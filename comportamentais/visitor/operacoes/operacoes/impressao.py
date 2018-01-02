class Impressora(object):
    """
    Navega na arvore de elementos (operaçoes) imprimindo a expressão ou
    expressões aninhadas
    """

    def visita_soma(self, soma):
        """
        Formata e imprime a operação de soma.
        """

        return "({0} + {1})".format(
            soma.expressao_esquerda.aceita(self),
            soma.expressao_direita.aceita(self)
        )

    def visita_subtracao(self, subtracao):
        """
        Formata e imprime a operação de subtração.
        """

        return "({0} - {1})".format(
            subtracao.expressao_esquerda.aceita(self),
            subtracao.expressao_direita.aceita(self)
        )

    def visita_multiplicacao(self, multiplicacao):
        """
        Formata e imprime a operação de multiplicação.
        """

        return "({0} x {1})".format(
            multiplicacao.expressao_esquerda.aceita(self),
            multiplicacao.expressao_direita.aceita(self)
        )

    def visita_divisao(self, divisao):
        """
        Formata e imprime a operação de divisão.
        """

        return "({0}/{1})".format(
            divisao.dividendo.aceita(self),
            divisao.divisor.aceita(self)
        )

    def visita_numero(self, numero):
        """
        Formata e imprime o número.
        """

        return numero.executa()
