from romanos.numeroRomanoInterpreter import NumeroRomanoInterpreter

class UmDigitoRomano(NumeroRomanoInterpreter):

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
