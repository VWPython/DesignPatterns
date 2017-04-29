class Compra(object):

    __contador_id = 0

    def __init__(self, nome_da_loja):
        self.nome_da_loja = nome_da_loja
        self.__contador_id += 1
        self.id_nota_fiscal = self.__contador_id

    def modifica_valor(self, valor):
        self.valor_total = valor

    def pega_informacao_da_nota_fiscal(self):
        informacao = "Nota fiscal n°: " + str(self.id_nota_fiscal) + "\nLoja: " + self.nome_da_loja + "\nValor: " + str(self.valor_total) + "\n"
        return informacao
