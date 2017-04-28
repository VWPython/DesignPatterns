from observador.dadosObserver import DadosObserver

class TabelaObserver(DadosObserver):

    def __init__(self, dados):
        super().__init__(dados)

    def atualiza(self):
        print("Tabela:")
        print("Valor A: " + str(self.dados.pega_estado().valorA))
        print("Valor B: " + str(self.dados.pega_estado().valorB))
        print("Valor C: " + str(self.dados.pega_estado().valorC))
