from romanos.gramatica import GramaticaDeNumerosRomanos


class UmDigitoRomano(GramaticaDeNumerosRomanos):
    """
    Gramática de números romanos de um digitos.
    """

    def um(self):
        return "I"

    def quatro(self):
        return "IV"

    def cinco(self):
        return "V"

    def nove(self):
        return "IX"

    def multiplicador(self):
        return 1
