from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def __eq__(self, other):
        pass

    @property # Getter
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    @abstractmethod
    def salario(self):
        pass


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_mes, precio_hora):
        super().__init__(nombre, apellido)
        self.__horas_mes = horas_mes
        self.__precio_hora = precio_hora

    @property
    def salario(self):
        return self.__horas_mes * self.__precio_hora


class Estudiante:
    def __init__(self, legajo):
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo


class EstudiantePasante(Empleado, Estudiante):
    def __init__(self, nombre, apellido, legajo):
        Empleado.__init__(self, nombre, apellido)
        Estudiante.__init__(self, legajo)

    @property
    def salario(self):
        return 0

# e1 = Empleado("Carlos", "Lopez")
# e2 = Empleado("Maria", "Del Cerro")
# print(e1.nombre_completo)

eft1 = EmpleadoFullTime("Martin", "Gomez", 1000)
eph1 = EmpleadoPorHora("Julia", "Martinez", 26, 50)
print(eft1.nombre_completo)
print(eft1.salario)

print(eph1.nombre_completo)
print(eph1.salario)

ep1 = EstudiantePasante("Gaston", "Perez", 100001)
print(ep1.legajo)