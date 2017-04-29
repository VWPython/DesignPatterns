from romanos.numeroRomanoInterpreter import NumeroRomanoInterpreter

class DoisDigitosRomanos(NumeroRomanoInterpreter):

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
