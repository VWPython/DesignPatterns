from car.factories.carFactory import CarFactory
from car.cars.gol import Gol

class Wolkswagen(CarFactory):

    def build_car(self):
        return Gol()
