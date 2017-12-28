from dados.observer import Observer


class Porcento(Observer):
    """
    Classe responsavel por observar os dados e imprimi-los em forma
    de percentagem.
    """

    def __init__(self, dados):
        """
        Inicializa os dados.
        """

        super().__init__(dados)

    def atualiza(self):
        """
        Pega os dados atuais e soma eles, imprimindo o resultado em forma
        de percentagem.
        """

        soma = self.dados.pega_estado().valorA + self.dados.pega_estado().valorB + self.dados.pega_estado().valorC

        print("Porcentagem:")
        print("Valor A: %.2f percento" % ((self.dados.pega_estado().valorA/soma)*100))
        print("Valor B: %.2f percento" % ((self.dados.pega_estado().valorB/soma)*100))
        print("Valor C: %.2f percento" % ((self.dados.pega_estado().valorC/soma)*100))
        print("\n")
