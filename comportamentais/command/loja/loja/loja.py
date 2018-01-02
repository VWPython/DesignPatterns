from loja.compra import Compra


class Loja(object):
    """
    Loja onde foi realizada a compra.
    """

    def __init__(self, nome):
        """
        Cria a loja.
        """

        self.nome_da_loja = nome

    def executa_compra(self, valor, forma_de_pagamento):
        """
        Executa a compra.
        """

        compra = Compra(self.nome_da_loja)
        compra.modifica_valor(valor)
        forma_de_pagamento.processa_compra(compra)
