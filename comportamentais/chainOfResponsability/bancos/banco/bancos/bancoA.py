from banco.bancoChain import BancoChain
from banco.idBancos import IDBancos


class BancoA(BancoChain):

    def __init__(self):
        super(BancoA, self).__init__(IDBancos.bancoA)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco A")
