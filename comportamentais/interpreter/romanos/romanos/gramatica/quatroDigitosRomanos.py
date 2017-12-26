from romanos.numeroRomanoInterpreter import NumeroRomanoInterpreter

class QuatroDigitosRomanos(NumeroRomanoInterpreter):

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
