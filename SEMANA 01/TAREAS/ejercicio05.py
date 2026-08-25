##Ejercicio numero 5 : Diseñar un Pseudocódigo, diagrama de flujo y programa en Python, donde ingreses tu altura y si la altura ingresada es menor o igual a 1.50 mostrar mensaje “Persona de altura baja”, si la altura está entre 1.51 y 1.70 mostrar mensaje “Persona de altura media” y si la altura es mayor de 1.70 mostrar mensaje “Persona alta”

print(" Bienvenido a FARMACIA ROJAS")
height = float(input("Ingrese su altura en metros: "))
if height <= 1.50:
    print("Persona de estatura baja")
elif height >= 1.51 and height <= 1.70:
    print("Persona de altura media")
else:
    print("Persona alta")