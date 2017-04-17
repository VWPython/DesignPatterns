from car.factories.fiat import Fiat
from car.factories.wolkswagen import Wolkswagen
from car.factories.ford import Ford
from car.factories.chevrolet import Chevrolet

def main():

    factory = Fiat()
    car = factory.build_car()
    car.show_information();

    factory = Wolkswagen()
    car = factory.build_car()
    car.show_information();

    factory = Ford()
    car = factory.build_car()
    car.show_information();

    factory = Chevrolet()
    car = factory.build_car()
    car.show_information();

if __name__ == "__main__":
    main()
