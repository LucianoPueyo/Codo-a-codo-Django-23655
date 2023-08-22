
try:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))

    assert b != 0, "El divisor no puede ser 0"

except AssertionError as ae:
    print(str(ae))