##Ejercicio numero 7: Desarrollar un programa que calcule el promedio (debe ingresar 3 notas) de un alumno para evaluar su rendimiento (Malo 0-10, Regular 11-13, Bueno 14- 17, Excelente 18-20) 

print("CALCULADOR DE PROMEDIO")
nota1 = float(input("Ingresa tu primera nota: "))
nota2 = float(input("Ingresa tu segunda nota: "))
nota3 = float(input("Ingresa tu tercera nota: "))
prom = (nota1 + nota2 + nota3)/3
if 0 <= prom <= 20:
    print(f"Tu promedio es {prom:.2f}")
    if prom <= 10.4:
        print("Rendimiento: Malo")
    elif prom <= 13.4:
        print("Rendimiento: Regular")
    elif prom <= 17.4:
        print("Rendimiento: Bueno")
    elif prom <= 20:
        print("Rendimiento: Excelente")
else:
        print("ERROR, INGRESAR NOTAS VALIDAS")
