from banco.bancoChain import BancoChain
from banco.idBancos import IDBancos


class BancoD(BancoChain):

    def __init__(self):
        super(BancoD, self).__init__(IDBancos.bancoD)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco D")
