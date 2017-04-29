from loja.compra import Compra

class Loja(object):

    def __init__(self, nome):
        self.nome_da_loja = nome

    def executa_compra(self, valor, forma_de_pagamento):
        compra = Compra(self.nome_da_loja)
        compra.modifica_valor(valor)
        forma_de_pagamento.processa_compra(compra)
