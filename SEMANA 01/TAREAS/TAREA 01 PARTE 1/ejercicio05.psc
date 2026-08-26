Algoritmo ClasificarAltura
    Definir height Como Real
    Escribir "Bienvenido a FARMACIA ROJAS"
    Escribir "Ingrese su altura en metros: "
    Leer height
    
    Si height <= 1.50 Entonces
        Escribir "Persona de altura baja"
    Sino
        Si height <= 1.70 Entonces
            Escribir "Persona de altura media"
        Sino
            Escribir "Persona alta"
        FinSi
    FinSi
FinAlgoritmo