from loja.pagamentoCommand import PagamentoCommand

class PagamentoCartaoDeDebito(PagamentoCommand):

    def processa_compra(self, compra):
        print("Cartão de debito aceito!\n" + compra.pega_informacao_da_nota_fiscal())
