from descontos.cinco_itens import DescontoCincoItens
from descontos.quinhentos_reais import DescontoQuinhentosReais
from descontos.sem_desconto import SemDesconto


class Calculador(object):
    """
    Calculador de descontos.
    """

    def calcula(self, orcamento):
        """
        Calcula o desconto da compra.
        """

        desconto = DescontoCincoItens(
            DescontoQuinhentosReais(
                SemDesconto()
            )
        ).calcula(orcamento)

        return desconto
