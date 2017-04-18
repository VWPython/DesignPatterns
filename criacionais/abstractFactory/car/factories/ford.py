from car.factories.carFactory import CarFactory
from car.cars.fiestaSedan import FiestaSedan
from car.cars.fiesta import Fiesta

class Ford(CarFactory):

    def build_sedan_car(self):
        return FiestaSedan()

    def build_popular_car(self):
        return Fiesta()
