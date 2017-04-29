from loja.pagamentoCommand import PagamentoCommand

class PagamentoBoleto(PagamentoCommand):

    def processa_compra(self, compra):
        print("Boleto criado!\n" + compra.pega_informacao_da_nota_fiscal())
