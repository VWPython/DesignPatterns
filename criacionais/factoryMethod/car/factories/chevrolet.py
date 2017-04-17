from car.factories.carFactory import CarFactory
from car.cars.celta import Celta

class Chevrolet(CarFactory):

    def build_car(self):
        return Celta()
