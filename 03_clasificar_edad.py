try:
    edad = float(input("Ingrese su edad: "))

    if edad <= 0:
        print("La edad debe ser mayor que cero.")
    elif edad < 18:
        print("Eres menor de edad.")
    elif edad <= 65:
        print("Eres adulto.")
    else:
        print("Eres adulto mayor.")
except ValueError:
    print("La edad debe ser numérica.")
