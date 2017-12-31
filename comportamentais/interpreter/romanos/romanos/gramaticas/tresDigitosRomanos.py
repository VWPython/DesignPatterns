from romanos.gramatica import GramaticaDeNumerosRomanos


class TresDigitosRomanos(GramaticaDeNumerosRomanos):
    """
    Gramática de números romanos de três digitos.
    """

    def um(self):
        return "C"

    def quatro(self):
        return "CD"

    def cinco(self):
        return "D"

    def nove(self):
        return "CM"

    def multiplicador(self):
        return 100
