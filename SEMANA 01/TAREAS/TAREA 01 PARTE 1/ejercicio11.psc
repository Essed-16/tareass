Algoritmo CalculadoraOperaciones
    Definir num1, num2, resultado Como Real
    Definir operacion Como Caracter
    
    Escribir "CALCULADOR DE OPERACIONES"
    Escribir "Ingresa el primer número: "
    Leer num1
    Escribir "Ingresa el segundo número: "
    Leer num2
    Escribir "Ingresa la operación a realizar (S para suma, R para resta, M para multiplicación, D para división): "
    Leer operacion
    
    operacion = Mayusculas(operacion)
    
    Si operacion == "S" Entonces
        resultado = num1 + num2
        Escribir "El resultado de la suma es: ", resultado
    Sino
        Si operacion == "R" Entonces
            resultado = num1 - num2
            Escribir "El resultado de la resta es: ", resultado
        Sino
            Si operacion == "M" Entonces
                resultado = num1 * num2
                Escribir "El resultado de la multiplicación es: ", resultado
            Sino
                Si operacion == "D" Entonces
                    Si num2 <> 0 Entonces
                        resultado = num1 / num2
                        Escribir "El resultado de la división es: ", resultado
                    Sino
                        Escribir "Error: No se puede dividir entre cero."
                    FinSi
                Sino
                    Escribir "Error: Operación no válida."
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo