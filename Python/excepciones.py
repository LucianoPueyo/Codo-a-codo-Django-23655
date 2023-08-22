while True:
    try:
        a = input("Ingrese un numero: ")
        b = input("Ingrese otro numero: ")

        if a.lower() == "salir" or b.lower() == "salir":
            break

        print(int(a) / int(b))

    except ZeroDivisionError as zde:
        print(str(zde), ": Por favor ingrese un divisor distinto de 0")

    except ValueError as ve:
        print(str(ve), "Por favor solo ingresar numeros enteros")

print("Adios")
