# Ejercicio 1
def mcd(a, b):
    while b:
        a, b = b, a % b

        # Misma solución usando un auxiliar
        # aux = a
        # a = b
        # b = aux % b

    return abs(a)

# Ejercicio 2
def mcm(a, b):
    return (a * b) / mcd(a,b)

# Ejercicio 3
def frecuencia(cadena):
    palabras = cadena.split(" ")

    resultado = {}
    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1

        else:
            resultado[palabra] = 1

    return resultado

#Ejercicio 4
def max_frecuencia(palabras):
    maximo = ("", 0)

    dicc_palabras = frecuencia(palabras)

    for palabra, frec in dicc_palabras.items():
        if frec > maximo[1]:
            maximo = palabra, frec

    return maximo

# Ejercicio 5
def get_int():
    while True:
        try:
            valor = int(input("Ingrese un numero: "))
            break

        except ValueError as ve:
            print("Dato invalido. Solo se aceptan numeros enteros")

    return valor

# Ejercicio 6

class Persona:
    ADULTEZ = 18

    def __init__(self, nombre, edad, DNI):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("Edad no puede ser negativa")

        if type(valor) is not int:
            raise TypeError("La edad deber ser un numero entero")

        self.__edad = valor

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, valor):
        self.__DNI = valor

    def mostrar(self):
        return f"{self.__nombre} {self.__edad} DNI: {self.__DNI}"

    def es_mayor_de_edad(self):
        return self.__edad >= Persona.ADULTEZ

    def __str__(self):
        return self.mostrar()
    
    def __repr__(self):
        return self.mostrar()


p1 = Persona("Carlos Lopez", 25, 1234)


#---------------------------------------------------------

# Tests
# Ejercicio 1
assert mcd(8,4) == 4, "Error"
assert mcd(4,8) == 4, "Error"
assert mcd(-15,-5) == 5, "Error"
assert mcd(13,8) == 1, "Error"

# Ejercicio 2
assert mcm(8,4) == 8, "Error"
assert mcm(4,8) == 8, "Error"
assert mcm(12,10) == 60, "Error"

# Ejercicio 3
assert frecuencia("hola") == {'hola': 1}, "Error"
assert frecuencia("hola hola hola") == {'hola': 3}, "Error"
assert frecuencia("Hola como estas mi nombre Luciano") == {'Hola': 1, 'como': 1, 'estas': 1, 'mi': 1, 'nombre': 1, 'Luciano': 1}, "Error"
assert frecuencia("Si Si si no no No No") == {'Si': 2, 'si': 1, 'no': 2, 'No': 2}, "Error"

# Ejercicio 4
assert max_frecuencia("a a a b b c") == ('a', 3), "Error"
assert max_frecuencia("a b c") == ('a', 1), "Error"
assert max_frecuencia("c b a") == ('c', 1), "Error"

# Ejercicio 5
# Como esta funcion implica entrada de usuario por consola, la voy a omitir
# get_int()

# Ejercicio 6

# Ejercicio 7

# Ejercicio 8


print("Todos los test OK")
