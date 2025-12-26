from io import BytesIO
from pypdf import PdfReader, PdfWriter

def compress_pdf(input_pdf_stream: BytesIO) -> BytesIO:
    """
    Comprime un archivo PDF en memoria usando pypdf.
    
    Args:
        input_pdf_stream (BytesIO): Stream del PDF original.
        
    Returns:
        BytesIO: Stream del PDF comprimido.
    """
    try:
        # Asegurarse de estar al inicio del stream
        input_pdf_stream.seek(0)
        
        reader = PdfReader(input_pdf_stream)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Aplicar compresión
        writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)
        
        # Reducir calidad de imágenes si es necesario (opcional, pypdf lo hace por defecto con compress_identical_objects en cierta medida)
        # Para mayor compresión de imágenes se requeriría re-procesarlas con Pillow, 
        # pero esto es un buen primer paso sin dependencias extra complejas.
        
        output_stream = BytesIO()
        writer.write(output_stream)
        output_stream.seek(0)
        
        return output_stream
    except Exception as e:
        # En caso de error, devolver el original sin comprimir para no romper el flujo
        print(f"Error comprimiendo PDF: {e}")
        input_pdf_stream.seek(0)
        return input_pdf_stream
