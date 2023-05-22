# Classes

class Car:
    def __init__(self, modelo, marca, anio) -> None:
        self.modelo = modelo
        self.marca = marca
        self.anio = anio

    def encender_motor(self):
        print("Este motor esta encendido")

    def apagar_motor(self):
        print("Este motor esta apagado")


class Electric(Car):
    def cargando_bateria(self):
        print("Este auto esta cargando bateria")

class Hibrido(Car):
    def motor_hibrido(self):
        print("Este motor funciona con gasolina o con bateria")

# Atributos
carro_01 = Electric('Prius', 'Toyota', 2023)
print(carro_01.modelo)
print(carro_01.marca)
print(carro_01.anio)

# Metodos
carro_01.encender_motor()
carro_01.apagar_motor()
carro_01.cargando_bateria()

# Atributos
carro_02 = Hibrido('Corolla', 'Toyota', 2022)
print(carro_02.modelo)
print(carro_02.marca)
print(carro_02.anio)

# Metodos
carro_02.encender_motor()
carro_02.apagar_motor()
carro_02.motor_hibrido()