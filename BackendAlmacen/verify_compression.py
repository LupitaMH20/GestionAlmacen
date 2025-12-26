import os
import sys
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Asegurar que podemos importar desde la carpeta de la aplicación
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from application.pdf.utils import compress_pdf

def generate_test_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, "Hello World - Test PDF Compression")
    
    # Agregar algo de contenido 'pesado' (texto repetitivo para simular)
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 50
    y = 700
    for _ in range(50):
        c.drawString(50, y, text[:100])
        y -= 12
        if y < 50:
            c.showPage()
            y = 700
            
    c.save()
    buffer.seek(0)
    return buffer

def main():
    print("Generando PDF de prueba...")
    original_pdf = generate_test_pdf()
    original_size = original_pdf.getbuffer().nbytes
    print(f"Tamaño original: {original_size} bytes")
    
    # Guardar original para referencia (opcional)
    # with open("test_original.pdf", "wb") as f:
    #     f.write(original_pdf.getvalue())
        
    print("Comprimiendo PDF...")
    compressed_pdf = compress_pdf(original_pdf)
    compressed_size = compressed_pdf.getbuffer().nbytes
    print(f"Tamaño comprimido: {compressed_size} bytes")
    
    # Guardar comprimido para referencia (opcional)
    # with open("test_compressed.pdf", "wb") as f:
    #     f.write(compressed_pdf.getvalue())
    
    reduction = original_size - compressed_size
    percentage = (reduction / original_size) * 100
    
    print(f"Reducción: {reduction} bytes ({percentage:.2f}%)")
    
    if compressed_size < original_size:
        print(" VERIFICACIÓN EXITOSA: El PDF se comprimió correctamente.")
    elif compressed_size == original_size:
         print(" VERIFICACIÓN NEUTRA: El PDF no cambió de tamaño (posiblemente porque ya es simple).")
    else:
        print(" VERIFICACIÓN FALLIDA: El PDF aumentó de tamaño (algo raro pasó).")

if __name__ == "__main__":
    main()
