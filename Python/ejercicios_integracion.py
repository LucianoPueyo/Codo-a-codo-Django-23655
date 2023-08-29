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


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        return f"Titular: {self.__titular.nombre} cantidad: {self.__cantidad}"
    
    def ingresar(self, monto):
        if monto <= 0:
            raise(ValueError, "El monto no puede ser 0 o menos")

        self.__cantidad += monto

    def retirar(self, monto):
        self.__cantidad -= monto


class CuentaJoven(Cuenta):
    def __init__(self, titular,  bonificacion, cantidad=0):
        super().__init__(titular, cantidad)

        self.__bonificacion = bonificacion
        
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25
    
    def retirar(self, monto):
        if not self.es_titular_valido():
            raise ValueError("Solo pueden retirar dinero titulares validos")

        return super().retirar(monto)
    
    def mostrar(self):
        return f"- Cuenta Joven - titular: {self.titular.nombre} - bonificacion: {self.__bonificacion}"

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
p1 = Persona("Carlos Lopez", 25, 1234)
assert p1.nombre == "Carlos Lopez", "Error"
assert p1.edad == 25, "Error"
assert p1.DNI == 1234, "Error"
assert p1.mostrar() == "Carlos Lopez 25 DNI: 1234", "Error"
assert p1.es_mayor_de_edad(), "Error"

# Ejercicio 7
p2 = Persona("Maria Del Cerro", 30, 4321)
c1 = Cuenta(p2)

assert c1.titular.nombre == "Maria Del Cerro", "Error"
assert c1.cantidad == 0.0, "Error"

c1.ingresar(1000.0)
assert c1.cantidad == 1000.0, "Error"

c1.retirar(750.0)
assert c1.cantidad == 250.0, "Error"

assert c1.mostrar() == "Titular: Maria Del Cerro cantidad: 250.0", "Error"

# Ejercicio 8
p3 = Persona("Gaston Gomez", 23, 9119)
cj1 = CuentaJoven(p3, .25, 1000.0)

cj1.retirar(500)
assert cj1.cantidad == 500.0, "Error"

p4 = Persona("Florencia Ramirez", 35, 1991)
cj2 = CuentaJoven(p4, .15, 1500.0)

try:
    cj2.retirar(500)

except ValueError as ve:
    assert str(ve) == "Solo pueden retirar dinero titulares validos"

print("Todos los test OK")
