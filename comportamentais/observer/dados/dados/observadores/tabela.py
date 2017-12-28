from dados.observer import Observer


class Tabela(Observer):
    """
    Classe responsavel por observar os dados e imprimi-los em forma de tabela.
    """

    def __init__(self, dados):
        """
        Inicializa os dados.
        """

        super().__init__(dados)

    def atualiza(self):
        """
        Mostra os dados em forma de tabela
        """

        print("Tabela:")
        print("Valor A: " + str(self.dados.pega_estado().valorA))
        print("Valor B: " + str(self.dados.pega_estado().valorB))
        print("Valor C: " + str(self.dados.pega_estado().valorC))
        print("\n")
