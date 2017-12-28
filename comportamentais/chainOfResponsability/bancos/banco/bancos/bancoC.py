from banco.bancoChain import BancoChain
from banco.idBancos import IDBancos


class BancoC(BancoChain):

    def __init__(self):
        super(BancoC, self).__init__(IDBancos.bancoC)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco C")
