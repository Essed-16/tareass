##Ejercicio numero 4: Diseñar un diagrama de flujo y programa en python que permita mostrar un mensaje indicando si un alumno está Aprobado o Desaprobado en el curso de ALGORITMIA PARA EL DESARROLLO DE PROGRAMAS. Para calcular el promedio final del curso se debe considerar: Tarea1, Tarea2 y Tarea3. Para aprobar el curso se necesita una nota mínima de 13

print("CURSO: ALGORITMIA PARA EL DESARROLLO DE PROGRAMAS")
nota1 = float(input("Ingresa tu primera nota: "))
nota2 = float(input("Ingresa tu segunda nota: "))
nota3 = float(input("Ingresa tu tercera nota: "))
prom = (nota1 + nota2 + nota3)/3
print(f"Tu promedio es {prom}")
if prom >= 13:
    print("Felicidades, aprobaste")
else:
    print("Has desaprobado, esfuerzate mas para la proxima")