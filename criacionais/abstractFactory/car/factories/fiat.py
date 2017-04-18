from car.factories.carFactory import CarFactory
from car.cars.siena import Siena
from car.cars.palio import Palio

class Fiat(CarFactory):

    def build_sedan_car(self):
        return Siena()

    def build_popular_car(self):
        return Palio()
