##Ejercicio numero 12: Desarrolle un algoritmo donde debemos ingresar la cantidad de alumnos a transportar y debemos calcular el costo total, sabiendo que por cada alumno el costo de transporte está en el siguiente rango. Imprime el costo a cobrar.

print("CALCULADOR DE COSTO DE TRANSPORTE")
alumnos = int(input("Ingresa la cantidad de alumnos a transportar: "))
if alumnos < 20:
    costo= 70
elif alumnos < 50:
    costo = 40
elif alumnos <= 100:
    costo = 35
else:
    costo = 20
print(f"El costo total a cobrar por el transporte de {alumnos} alumnos es: s/.{costo * alumnos}")