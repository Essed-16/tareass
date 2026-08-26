##Desarrolle un algoritmo y muestra la solución en pseudocódigo, diagrama de flujo y ejecución en Python, que permita ingresar una clave. Si la clave es senati$2025, muestra como resultado los mensajes: “Clave correcta” y “Usuario autorizado” (5 puntos)

print("Bienvenido al sistema de inicio de sesión")
intentos = 3

while intentos > 0:
    usuario = input("Ingrese su nombre de usuario: ").lower()
    clave = input("Ingrese su clave: ")

    if usuario == "alumno-senati" and clave == "senati$2025":
        print("Clave correcta")
        print("Usuario autorizado")
        break
    else:
        intentos -= 1
        print(f"Clave incorrecta. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Has agotado tus intentos. El sistema se cerrará.")