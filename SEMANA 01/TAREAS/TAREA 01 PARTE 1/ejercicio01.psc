Algoritmo operacionesbasicas
	Definir num1, num2 Como Real
    
    Escribir "Ingrese el primer numero: "
    Leer num1
    Escribir "Ingrese el segundo numero: "
    Leer num2
    
    Escribir "La suma de los dos numeros es ", (num1 + num2)
    Escribir "La resta de los dos numeros es ", (num1 - num2)
    Escribir "El producto de los dos numeros es ", (num1 * num2)
    
    Si num2 <> 0 Entonces
        Escribir "La division de los dos numeros es ", (num1 / num2)
        Escribir "El resto entero de los dos numeros es ", (num1 % num2)
    Sino
        Escribir "Error: No se puede dividir entre cero."
    FinSi
FinAlgoritmo
