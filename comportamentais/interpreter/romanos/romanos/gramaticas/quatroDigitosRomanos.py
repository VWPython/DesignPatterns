from romanos.gramatica import GramaticaDeNumerosRomanos


class QuatroDigitosRomanos(GramaticaDeNumerosRomanos):
    """
    Gramática de números romanos de quatro digitos.
    """

    def um(self):
        return "M"

    def quatro(self):
        return " "

    def cinco(self):
        return " "

    def nove(self):
        return " "

    def multiplicador(self):
        return 1000
