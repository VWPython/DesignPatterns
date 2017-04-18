from car.factories.fiat import Fiat
from car.factories.ford import Ford


def main():

    factory = Fiat()
    sedan = factory.build_sedan_car()
    popular = factory.build_popular_car()
    sedan.show_information()
    popular.show_information()

    factory = Ford()
    sedan = factory.build_sedan_car()
    popular = factory.build_popular_car()
    sedan.show_information()
    popular.show_information()

if __name__ == "__main__":
    main()
