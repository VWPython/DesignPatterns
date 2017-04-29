from loja.pagamentoCommand import PagamentoCommand

class PagamentoCartaoDeCredito(PagamentoCommand):

    def processa_compra(self, compra):
        print("Cartão de credito aceito!\n" + compra.pega_informacao_da_nota_fiscal())
