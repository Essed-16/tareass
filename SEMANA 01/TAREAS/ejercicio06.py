##Ejercicio numero 6: Diseñar un algoritmo que permita ingresar un número entero. Se desea saber si es “Par” o “Impar” (Par: var_numero%2==0)

print("=====  Descubre si tu numero es par  =====")
num = int(input("Ingresa tu numero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")