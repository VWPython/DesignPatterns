from romanos.numeroRomanoInterpreter import NumeroRomanoInterpreter

class TresDigitosRomanos(NumeroRomanoInterpreter):

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
