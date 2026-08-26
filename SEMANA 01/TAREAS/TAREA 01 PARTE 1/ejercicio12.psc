Algoritmo CostoTransporte
    Definir alumnos Como Entero
    Definir costo Como Real
    
    Escribir "CALCULADOR DE COSTO DE TRANSPORTE"
    Escribir "Ingresa la cantidad de alumnos a transportar: "
    Leer alumnos
    
    Si alumnos < 20 Entonces
        costo = 70
    Sino
        Si alumnos < 50 Entonces
            costo = 40
        Sino
            Si alumnos <= 100 Entonces
                costo = 35
            Sino
                costo = 20
            FinSi
        FinSi
    FinSi
    
    Escribir "El costo total a cobrar por el transporte de ", alumnos, " alumnos es: s/.", (costo * alumnos)
FinAlgoritmo