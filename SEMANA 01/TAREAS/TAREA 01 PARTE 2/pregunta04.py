##Desarrolle un algoritmo y muestra la solución en pseudocódigo, diagrama de flujo y ejecución en Python, que permita ingresar dos valores distintos y determinar cuál de los dos valores es el mayor y escribirlo. (5 puntos)

valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

if valor1 > valor2:
    print(f"El mayor valor es: {valor1}")
elif valor2 > valor1:
    print(f"El mayor valor es: {valor2}")
else:
    print("Los valores son iguales.")