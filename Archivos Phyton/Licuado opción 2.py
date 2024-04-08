# Programa para ordenar un licuado de fresa con opciones personalizadas

# Función principal
def main():
    # Solicitar el nombre y apellido del usuario
    nombre = input("Por favor, introduce tu nombre: ")
    NIT = input("Ahora, introduce tu NIT: ")
    
    # Detalles del pedido por defecto
    licuado = "Licuado de fresa con leche deslactosada sin azúcar"
    precio_base = 20.00
    
    # Opciones de azúcar
    print("¿Deseas agregar azúcar a tu licuado? (0, 1 o 2 cucharadas)")
    cucharadas_azucar = int(input("Introduce la cantidad de cucharadas de azúcar: "))
    
    # Validar la cantidad de azúcar
    while cucharadas_azucar < 0 or cucharadas_azucar > 2:
        print("Solo puedes agregar hasta dos cucharadas de azúcar.")
        cucharadas_azucar = int(input("Introduce la cantidad correcta de cucharadas de azúcar: "))
    
    # Calcular el precio final
    precio_final = precio_base + (cucharadas_azucar * 0.50)
    
    # Mostrar el resumen del pedido
    print(f"\nResumen del pedido para {nombre} {NIT}:")
    print(f"Producto: {licuado}")
    print(f"Cantidad de azúcar: {cucharadas_azucar} cucharada(s)")
    print(f"Total a pagar: Q{precio_final:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()