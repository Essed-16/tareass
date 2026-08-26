Algoritmo CalcularPromedioRendimiento
    Definir nota1, nota2, nota3, prom Como Real
    
    Escribir "CALCULADOR DE PROMEDIO"
    Escribir "Ingresa tu primera nota: "
    Leer nota1
    Escribir "Ingresa tu segunda nota: "
    Leer nota2
    Escribir "Ingresa tu tercera nota: "
    Leer nota3
    
    prom = (nota1 + nota2 + nota3) / 3
    
    Si prom >= 0 Y prom <= 20 Entonces
        Escribir "Tu promedio es: ", prom
        
        Si prom <= 10.4 Entonces
            Escribir "Rendimiento: Malo"
        Sino
            Si prom <= 13.4 Entonces
                Escribir "Rendimiento: Regular"
            Sino
                Si prom <= 17.4 Entonces
                    Escribir "Rendimiento: Bueno"
                Sino
                    Escribir "Rendimiento: Excelente"
                FinSi
            FinSi
        FinSi
    Sino
        Escribir "ERROR, INGRESAR NOTAS VALIDAS"
    FinSi
FinAlgoritmo