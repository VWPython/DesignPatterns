from observador.dadosObserver import DadosObserver

class PorcentoObserver(DadosObserver):

    def __init__(self, dados):
        super().__init__(dados)

    def atualiza(self):
        soma = self.dados.pega_estado().valorA + self.dados.pega_estado().valorB + self.dados.pega_estado().valorC
        print("Porcentagem:")
        print("Valor A:", str((self.dados.pega_estado().valorA/soma)*100))
        print("Valor B:", str((self.dados.pega_estado().valorB/soma)*100))
        print("Valor C:", str((self.dados.pega_estado().valorC/soma)*100))
