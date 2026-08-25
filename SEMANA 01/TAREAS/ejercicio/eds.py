import random
print("=============TE APUESTO============")
print("ELIGE TU EQUIPO\nOPCION 1: BOTAFOGO x1.12\nOPCION 2: EMPATE x8.9\nOPCION 3: CIENCIANO x22")
opcion = int(input("Elige la opcion 1, 2 o 3: "))
if opcion < 1 or opcion > 3:
    print("Elige una opcion valida¡¡¡¡")
else:
    monto = float(input("Ingresa el monto a apostar: "))
    resultado = random.randint(1, 3)
    print("==================")
    if resultado == 1:
        print("GANA BOTAFAGO")
    elif resultado == 2:
        print("EMPATE")
    elif resultado == 3:
        print("GANO CIENCIANO")
    print("==================")
if opcion == resultado:
    if opcion == 1:
        premio = monto * 1.12
    elif opcion == 2:
        premio = monto * 8
    elif opcion ==3:
        premio = monto * 22
    print("Felicidades, ganaste s/", premio)
else:
    print("Perdiste")
    
