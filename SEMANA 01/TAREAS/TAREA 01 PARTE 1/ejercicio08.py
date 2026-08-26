##Ejercicio numero 8: Dado el siguiente Diagrama de Flujo, elabora el correspondiente Pseudocódigo Y PYTHON

print("Calculador de importe por fotos")
fotos = int(input("Ingresa la cantidad de fotos: "))
if fotos < 10:
    precio = 1.50
elif fotos <= 30:
    precio = 1.00
else:
    precio = 0.50
importe = fotos * precio
print(f"Su precio por foto es: {precio:.2f}\nEl importe a pagar es: {importe:.2f}")