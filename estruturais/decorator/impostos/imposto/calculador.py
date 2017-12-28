class CalculadorDeImpostos(object):
    """
    Calcula o imposto gerado.
    """

    def realize_calculo(self, orcamento, imposto):
        """
        Realiza o calculo do imposto.
        """

        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)
