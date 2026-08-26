##Ejercicio 11: Desarrolle un algoritmo donde pida ingresar 2 números y la operación a calcular. La operación “S” debe realizar la suma. La operación “R” deber realizar la resta La operación “M” debe realizar la multiplicación. La operación “D” debe realizar la división. Imprime el resultado calculado.

print("CALCULADOR DE OPERACIONES")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación a realizar (S para suma, R para resta, M para multiplicación, D para división): ").upper()

if operacion == "S":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "R":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "M":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "D":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operación no válida.")