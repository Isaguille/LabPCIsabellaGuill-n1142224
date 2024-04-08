print ("Ejercicio 1: operaciones aritméticas")

#Entradas
numero1  = int(input("Ingrese un número entero"))
numero2  = int(input("Ingrese otro número entero"))

#Operaciones
divisionEntera  = numero1  //  numero2
divisionModular  = numero1 % numero2
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

#Salidas
print(numero1, "//", numero2, "=", divisionEntera)
print(numero1, "%", numero2, "=", divisionModular)
print(numero1, "+", numero2, "=", suma)
print(numero1, "-", numero2, "=", resta)
print(numero1, "*", numero2, "=", multiplicacion)

#Ejercicio 2
print ("Ejercicio 2: operaciones booleanas")

mayor_que = numero1 > numero2
menor_que = numero1 < numero2
igualdad = numero1 == numero2
diferencia  = numero1 != numero2

print(f"{numero1} > {numero2} = {mayor_que}")
print(f"{numero1} < {numero2} = {menor_que}")
print(f"{numero1} == {numero2} = {igualdad}")
print(f"{numero1} != {numero2} = {diferencia}")

#Ejercicio 3 
print ("Ejercicio 3: jerarquía de operadores")
a= int(input("Ingrese el valor de a: "))
b= int(input("Ingrese el valor de b: "))
c= int(input("Ingrese el valor de c: "))

expresion1 = a * b + c
expresion2 = a * (b + c)
expresion3 = a * b + c
expresion4 = 3 * a + 2 * b

print(f"a * b + c = {expresion1}")
print(f"a(b + c) = {expresion2}")
print(f"a b + c = {expresion3}")
print(f"3a + 2b = {expresion4}")
