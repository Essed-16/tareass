##Ejercicio numero 10: Desarrolle un algoritmo donde ingreses los lados de un triángulo y debemos indicar si es triángulo equilátero (3 lados miden igual), isósceles (2 lados son iguales y el otro mide distinto) o escaleno (los 3 miden distinto).

print("CALCULADOR DE TIPO DE TRIANGULO")
lado1 = float(input("Ingresa el primer lado del triángulo: "))
lado2 = float(input("Ingresa el segundo lado del triángulo: "))
lado3 = float(input("Ingresa el tercer lado del triángulo: "))
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
else:
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")