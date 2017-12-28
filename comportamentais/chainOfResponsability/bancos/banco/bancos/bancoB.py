from banco.bancoChain import BancoChain
from banco.idBancos import IDBancos


class BancoB(BancoChain):

    def __init__(self):
        super(BancoB, self).__init__(IDBancos.bancoB)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco B")
