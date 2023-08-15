x = 15
VARIABLE_GLOBAL_1 = 1

def funcion1():
    """
        Esto es un docstring.
        Un docstring permite agregar documentación a distintas partes en python.
    """
    print("Invocando funcion 1")
    print(x)
    y = 30

    def funcion_interna():
        print("Invocando funcion interna")
        x = 30
        print(x)

    funcion_interna()

funcion1()
print(x)

#print(y)