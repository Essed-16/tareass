Algoritmo EstadoAlumno
    Definir nota1, nota2, nota3, prom Como Real
    
    Escribir "CURSO: ALGORITMIA PARA EL DESARROLLO DE PROGRAMAS"
    Escribir "Ingresa tu primera nota: "
    Leer nota1
    Escribir "Ingresa tu segunda nota: "
    Leer nota2
    Escribir "Ingresa tu tercera nota: "
    Leer nota3
    
    prom <- (nota1 + nota2 + nota3) / 3
    
    Escribir "Tu promedio es ", prom
    
    Si prom >= 13 Entonces
        Escribir "Felicidades, aprobaste"
    Sino
        Escribir "Has desaprobado, esfuerzate mas para la proxima"
    FinSi
FinAlgoritmo