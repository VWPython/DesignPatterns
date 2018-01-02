class Compra(object):
    """
    Compra do cliente.
    """

    ID = 0

    def __init__(self, nome_da_loja):
        """
        Cria a compra do cliente.
        """

        self.nome_da_loja = nome_da_loja
        Compra.ID += 1
        self.id_nota_fiscal = Compra.ID

    def modifica_valor(self, valor):
        """
        Modifica o valor da compra.
        """

        self.valor_total = valor

    @property
    def nota_fiscal(self):
        """
        Pega informações da nota fiscal.
        """

        informacao = "Nota fiscal n° {0}\nLoja: {1}\nValor: {2}\n".format(
            str(self.id_nota_fiscal),
            self.nome_da_loja,
            str(self.valor_total)
        )

        return informacao
