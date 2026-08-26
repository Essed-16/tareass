Algoritmo DeterminarMayor
    Definir valor1, valor2 Como Real
    
    Escribir "Ingrese el primer valor: "
    Leer valor1
    Escribir "Ingrese el segundo valor: "
    Leer valor2
    
    Si valor1 > valor2 Entonces
        Escribir "El mayor valor es: ", valor1
    Sino
        Si valor2 > valor1 Entonces
            Escribir "El mayor valor es: ", valor2
        Sino
            Escribir "Los valores son iguales."
        FinSi
    FinSi
FinAlgoritmo