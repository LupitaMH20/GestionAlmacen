"""
Servicio para manejar almacenamiento de PDFs en Supabase Storage.
"""

import logging
from typing import Optional
from supabase import create_client, Client
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile

logger = logging.getLogger(__name__)


class SupabaseStoragePDF:
    """Cliente para interactuar con Supabase Storage - Solo PDFs."""

    def __init__(self):
        self.url = settings.SUPABASE_URL
        self.key = settings.SUPABASE_KEY
        self.bucket = settings.SUPABASE_BUCKET_DOCUMENTS

        if not self.url or not self.key:
            raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar configurados")

        logger.info(f"✅ SupabaseStorage inicializado: {self.url}")
        self.client: Client = create_client(self.url, self.key)

    def upload_pdf(
        self,
        file: UploadedFile,
        path: str,
    ) -> dict:
        """
        Sube un PDF a Supabase Storage.

        Args:
            file: Archivo PDF a subir
            path: Ruta dentro del bucket (ej: "solicitudes/2025/documento.pdf")

        Returns:
            Dict con información del archivo subido:
            {
                "success": True/False,
                "path": "ruta/archivo.pdf",
                "url": "https://...",
                "bucket": "documents",
                "size": 12345,
                "error": "mensaje de error" (solo si success=False)
            }
        """
        logger.info("=" * 60)
        logger.info(f"📄 Subiendo PDF: {path}")
        logger.info(f"  📦 Bucket: {self.bucket}")
        logger.info(f"  📏 Tamaño: {file.size if hasattr(file, 'size') else 'desconocido'}")

        try:
            # Leer el archivo PDF
            file.seek(0)
            file_data = file.read()

            if not file_data or len(file_data) == 0:
                logger.error("  ❌ ERROR: El archivo está vacío")
                return {"success": False, "error": "El archivo está vacío"}

            logger.info(f"  📊 Bytes a subir: {len(file_data)}")

            # Subir a Supabase
            logger.info("  🚀 Subiendo a Supabase...")
            response = self.client.storage.from_(self.bucket).upload(
                path=path,
                file=file_data,
                file_options={
                    "content-type": "application/pdf",
                    "upsert": "true"  # Sobrescribe si ya existe
                },
            )

            logger.info(f"  📨 Respuesta de Supabase: {response}")

            # Verificar respuesta
            if response is None:
                logger.error("  ❌ Supabase devolvió None")
                return {
                    "success": False,
                    "error": "Supabase no respondió correctamente"
                }

            # Verificar errores en la respuesta
            if isinstance(response, dict):
                if "error" in response:
                    error_msg = response.get("error", {})
                    logger.error(f"  ❌ Error en respuesta: {error_msg}")
                    return {"success": False, "error": str(error_msg)}

                if response.get("statusCode") and str(response.get("statusCode")).startswith(("4", "5")):
                    error_msg = response.get("message", response.get("error", "Error desconocido"))
                    logger.error(f"  ❌ HTTP {response.get('statusCode')}: {error_msg}")
                    return {
                        "success": False,
                        "error": f"HTTP {response.get('statusCode')}: {error_msg}"
                    }

            # Verificar que el archivo existe
            try:
                logger.info("  🔍 Verificando archivo en Supabase...")
                folder_path = path.rsplit("/", 1)[0] if "/" in path else ""
                list_response = self.client.storage.from_(self.bucket).list(path=folder_path)

                filename = path.rsplit("/", 1)[-1]
                file_exists = any(f.get("name") == filename for f in (list_response or []))

                if not file_exists:
                    logger.error(f"  ❌ Archivo no encontrado después de subir")
                    return {
                        "success": False,
                        "error": "El archivo no se encontró después de subir"
                    }

                logger.info(f"  ✅ Archivo verificado: {filename}")

            except Exception as verify_error:
                logger.warning(f"  ⚠️ No se pudo verificar el archivo: {verify_error}")

            # Obtener URL pública
            public_url = self.client.storage.from_(self.bucket).get_public_url(path)
            logger.info(f"  🔗 URL pública: {public_url}")

            result = {
                "success": True,
                "path": path,
                "url": public_url,
                "bucket": self.bucket,
                "size": len(file_data),
            }

            logger.info("  ✅ PDF SUBIDO EXITOSAMENTE")
            logger.info("=" * 60)

            return result

        except Exception as e:
            logger.error("=" * 60)
            logger.error(f"  ❌ ERROR SUBIENDO PDF: {str(e)}")
            logger.error("=" * 60)

            import traceback
            logger.error(traceback.format_exc())

            return {"success": False, "error": str(e)}

    def get_signed_url(
        self,
        path: str,
        expires_in: int = 3600
    ) -> Optional[str]:
        """
        Genera una URL firmada temporal para PDFs privados.

        Args:
            path: Ruta del archivo
            expires_in: Tiempo de expiración en segundos (default: 1 hora)

        Returns:
            URL firmada o None si hay error
        """
        try:
            response = self.client.storage.from_(self.bucket).create_signed_url(
                path=path,
                expires_in=expires_in
            )
            return response.get("signedURL") if response else None
        except Exception as e:
            logger.error(f"❌ Error generando signed URL: {e}")
            return None

    def delete_pdf(self, path: str) -> bool:
        """
        Elimina un PDF de Supabase Storage.

        Args:
            path: Ruta del archivo

        Returns:
            True si se eliminó correctamente
        """
        try:
            self.client.storage.from_(self.bucket).remove([path])
            logger.info(f"✅ PDF eliminado: {path}")
            return True
        except Exception as e:
            logger.error(f"❌ Error eliminando PDF: {e}")
            return False

    def list_pdfs(self, folder: str = "") -> list:
        """
        Lista PDFs en una carpeta del bucket.

        Args:
            folder: Carpeta a listar (vacío para raíz)

        Returns:
            Lista de archivos
        """
        try:
            files = self.client.storage.from_(self.bucket).list(folder)
            return files
        except Exception as e:
            logger.error(f"❌ Error listando PDFs: {e}")
            return []


from django.utils.functional import SimpleLazyObject

# ... (SupabaseStoragePDF class definition remains the same) ...

# Instancia global LAZY para evitar inicialización en startup
def get_supabase_storage():
    return SupabaseStoragePDF()

supabase_storage = SimpleLazyObject(get_supabase_storage)