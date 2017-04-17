from car.factories.carFactory import CarFactory
from car.cars.palio import Palio

class Fiat(CarFactory):

    def build_car(self):
        return Palio()
