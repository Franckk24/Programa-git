from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_fill_color(200, 220, 255)  # Color de fondo
        self.rect(0, 0, 210, 30, 'F')  # Rectángulo de fondo
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Factura", 0, 1, "C", 1)
        self.set_font("Arial", "I", 12)
        self.cell(0, 10, "Detalle de compra", 0, 1, "C", 1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def product_row(self, nombre, cantidad, precio_unitario, total):
        self.cell(100, 10, nombre, 1)
        self.cell(30, 10, str(cantidad), 1, 0, 'C')
        self.cell(30, 10, f"{precio_unitario:.2f}", 1, 0, 'C')
        self.cell(30, 10, f"{total:.2f}", 1, 1, 'C')

# Función principal
def main():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    fecha_factura = datetime.now().strftime("%d/%m/%Y")

    productos = []
    total_general = 0

    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))

        total_producto = cantidad * precio_unitario
        productos.append((nombre_producto, cantidad, precio_unitario, total_producto))
        total_general += total_producto

    # Imprimir resumen por consola
    print("\nResumen de la factura:")
    print(f"Nombre del cliente: {nombre_cliente}")
    print(f"Fecha de la factura: {fecha_factura}")
    print("Productos:")
    for producto in productos:
        print(f" - {producto[0]}: {producto[1]} x {producto[2]:.2f} = {producto[3]:.2f}")
    print(f"Total general: {total_general:.2f}")

    # Generar el PDF
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Nombre del cliente: {nombre_cliente}", 0, 1)
    pdf.cell(0, 10, f"Fecha de la factura: {fecha_factura}", 0, 1)
    pdf.cell(0, 10, "", 0, 1)  # Espacio en blanco

    # Encabezado de la tabla
    pdf.set_fill_color(255, 200, 200)  # Color de fondo de la tabla
    pdf.set_font("Arial", "B", 12)
    pdf.cell(100, 10, "Producto", 1, 0, 'C', 1)
    pdf.cell(30, 10, "Cantidad", 1, 0, 'C', 1)
    pdf.cell(30, 10, "Precio Unit.", 1, 0, 'C', 1)
    pdf.cell(30, 10, "Total", 1, 1, 'C', 1)

    pdf.set_font("Arial", "", 10)
    for producto in productos:
        pdf.product_row(producto[0], producto[1], producto[2], producto[3])

    pdf.cell(0, 10, "", 0, 1)  # Espacio en blanco
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Total general: {total_general:.2f}", 0, 1)

    # Guardar el PDF
    pdf.output("factura.pdf")
    print("Factura generada como 'factura.pdf'.")

if __name__ == "__main__":
    main()
