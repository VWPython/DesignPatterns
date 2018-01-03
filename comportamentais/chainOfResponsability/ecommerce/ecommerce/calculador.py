from ecommerce.descontos import (
    DescontoCincoItens, DescontoQuinhentosReais, SemDesconto
)


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
