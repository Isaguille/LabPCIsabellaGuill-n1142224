# Programa para realizar un pedido de licuado personalizado
def calcular_precio(base, azucar, leche, agrandar):
    precio = base
    precio += azucar * 0.50  # Costo adicional por azúcar
    if leche == 'agua':
        precio -= 2.00  # Descuento por elegir agua
    elif leche == 'soya':
        precio += 3.00  # Costo adicional por leche de soya
    if agrandar:
        precio *= 1.05  # Aumento del 5% por agrandar el licuado
    return precio

def main():
    nombre = input("Introduce tu nombre: ")
    NIT = input("Introduce tu NIT: ")
    print(f"Hola {nombre} - {NIT}, bienvenido al sistema de pedidos de licuados.")
   
    print("MENU STRAWBERRY SHAKE´S", "a. CANTIDAD DE AZÚCAR", "- Una cucharada-------Q 0.50", "- Dos cucharadas------Q 1.00 ", "b. TIPO DE LECHE", "- Con agua, sin leche----------------descuento Q 2.00", "- Leche entera/deslactosada----------No afecta precio", "- Soya-----------------------------------------Q 3.00", "c. TAMAÑO", "- Agrandado deL licuado-----Aumenta 5% de su precio", sep="\n")
   
    # Detalles del pedido por defecto
    base = 20.00
    azucar = int(input("¿Cuántas cucharadas de azúcar deseas agregar (0-2)? "))
    while azucar not in [0, 1, 2]:
        print("Solo puedes agregar hasta dos cucharadas de azúcar.")
        azucar = int(input("Introduce la cantidad correcta de cucharadas de azúcar: "))
    
    leche = input("Elige el tipo de leche (agua, deslactosada, entera, soya): ")
    while leche not in ['agua', 'deslactosada', 'entera', 'soya']:
        print("Opción no válida. Por favor, elige entre agua, deslactosada, entera o soya.")
        leche = input("Elige el tipo de leche: ")
    
    agrandar_respuesta = input("¿Deseas agrandar tu licuado (si/no)? ")
    agrandar = agrandar_respuesta.lower() == 'si'
    
    # Calcular el precio
    precio_final = calcular_precio(base, azucar, leche, agrandar)
    
    # Confirmar detalles del pedido
    print("\nDetalles de tu pedido:")
    print(f"Azúcar: {azucar} cucharada(s)")
    print(f"Tipo de leche: {leche}")
    print(f"Agrandado: {'Si' if agrandar else 'No'}")
    print(f"Precio total: Q{precio_final:.2f}")
    
    confirmar = input("¿Es correcta esta información? (si/no): ")
    if confirmar.lower() != 'si':
        print("Por favor, inicia de nuevo el proceso de pedido.")
        main()  # Reiniciar el proceso de pedido
    else:
        # Imprimir los detalles finales del pedido
        print("\nConfirmación del pedido:")
        print(f"Nombre: {nombre} - {NIT}")
        print(f"Licuado de fresa con leche {leche} {'y azúcar' if azucar > 0 else 'sin azúcar'}")
        print(f"{'Agrandado' if agrandar else 'Tamaño normal'}")
        print(f"Precio final: Q{precio_final:.2f}")

main()