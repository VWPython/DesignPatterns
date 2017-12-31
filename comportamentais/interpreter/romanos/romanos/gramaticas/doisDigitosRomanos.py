from romanos.gramatica import GramaticaDeNumerosRomanos


class DoisDigitosRomanos(GramaticaDeNumerosRomanos):
    """
    Gramática de números romanos de dois digitos.
    """

    def um(self):
        return "X"

    def quatro(self):
        return "XL"

    def cinco(self):
        return "L"

    def nove(self):
        return "XC"

    def multiplicador(self):
        return 10
