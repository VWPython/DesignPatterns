from car.factories.carFactory import CarFactory
from car.cars.fiesta import Fiesta

class Ford(CarFactory):

    def build_car(self):
        return Fiesta()
