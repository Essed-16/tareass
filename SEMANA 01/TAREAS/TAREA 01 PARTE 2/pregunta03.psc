Algoritmo SistemaLoginConIntentos
    Definir usuario, clave Como Caracter
    Definir intentos Como Entero
    
    Escribir "Bienvenido al sistema de inicio de sesión"
    intentos = 3
    
    Mientras intentos > 0 Hacer
        Escribir "Ingrese su nombre de usuario: "
        Leer usuario
        Escribir "Ingrese su clave: "
        Leer clave
        
        Si usuario == "alumno-senati" Y clave == "senati$2025" Entonces
            Escribir "Clave correcta"
            Escribir "Usuario autorizado"
            intentos = 0 
        Sino
            intentos = intentos - 1
            Escribir "Clave incorrecta. Te quedan ", intentos, " intentos."
        FinSi
    FinMientras
    
    Si intentos == 0 Y clave <> "senati$2025" Entonces
        Escribir "Has agotado tus intentos. El sistema se cerrará."
    FinSi
FinAlgoritmo