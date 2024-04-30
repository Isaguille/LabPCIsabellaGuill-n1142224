#Actividad no. 02
x = 0
y = 0

def MoverPosicion(cantX, CantY):
    global x, y
    x += cantX
    y += CantY

opcion = 'a'
while(opcion != 'e'):
    print("Semana No. 12: Ejercicio")
    print("Menú")
    print("a. Sube", "b. Baja", "c. Izquierda", "d. Derecha", "e. Salir", sep = "\t\n")
    opcion = input("Ingrese su opción: ")

    match opcion:
        case 'a':
            MoverPosicion(0, 1)
        case 'b':
            MoverPosicion(0, -1)
        case 'c':
            MoverPosicion(-1, 0)
        case 'd':
            MoverPosicion(1, 0)
        case _:
            print("Error: debe de ingresar una letra a-e") 

    print(f"La posición actual es: [{x}][{y}]")

    #Actividad no. 01

    import math

def ObtenerAreaTriangulo(b, h):
    return (b * h) / 2

def ObtenerAreaCuadrado(L):
    return L * L

def ObtenerAreaRectangulo(b, h):
    return b * h

def ObtenerAreaCirculo(r):
    return math.pi * r * r

def menu():
    print("Semana No. 12: Ejercicio 1")
    print("Selecciona la figura para calcular el área:")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    opcion = input("Ingresa la opción deseada (a, b, c, d): ")
    return opcion

def main():
    opcion = menu()
    if opcion == 'a':
        b = float(input("Ingresa la base del triángulo: "))
        h = float(input("Ingresa la altura del triángulo: "))
        area = ObtenerAreaTriangulo(b, h)
        print(f"El área del triángulo es: {area}")
    elif opcion == 'b':
        L = float(input("Ingresa el lado del cuadrado: "))
        area = ObtenerAreaCuadrado(L)
        print(f"El área del cuadrado es: {area}")
    elif opcion == 'c':
        b = float(input("Ingresa la base del rectángulo: "))
        h = float(input("Ingresa la altura del rectángulo: "))
        area = ObtenerAreaRectangulo(b, h)
        print(f"El área del rectángulo es: {area}")
    elif opcion == 'd':
        r = float(input("Ingresa el radio del círculo: "))
        area = ObtenerAreaCirculo(r)
        print(f"El área del círculo es: {area}")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()