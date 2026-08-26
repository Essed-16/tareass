Algoritmo TipoTriangulo
    Definir lado1, lado2, lado3 Como Real
    
    Escribir "CALCULADOR DE TIPO DE TRIANGULO"
    Escribir "Ingresa el primer lado del triángulo: "
    Leer lado1
    Escribir "Ingresa el segundo lado del triángulo: "
    Leer lado2
    Escribir "Ingresa el tercer lado del triángulo: "
    Leer lado3
    
    Si lado1 == lado2 Y lado2 == lado3 Entonces
        Escribir "El triángulo es equilátero"
    Sino
        Si lado1 == lado2 O lado1 == lado3 O lado2 == lado3 Entonces
            Escribir "El triángulo es isósceles"
        Sino
            Escribir "El triángulo es escaleno"
        FinSi
    FinSi
FinAlgoritmo