Algoritmo CalcularImporteFotos
    Definir fotos Como Entero
    Definir precio, importe Como Real
    
    Escribir "Calculador de importe por fotos"
    Escribir "Ingresa la cantidad de fotos: "
    Leer fotos
    
    Si fotos < 10 Entonces
        precio = 1.50
    Sino
        Si fotos <= 30 Entonces
            precio = 1.00
        Sino
            precio = 0.50
        FinSi
    FinSi
    
    importe = fotos * precio
    
    Escribir "Su precio por foto es: ", precio
    Escribir "El importe a pagar es: ", importe
FinAlgoritmo