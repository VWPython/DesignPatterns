from ecommerce.bancoChain import BancoChain
from ecommerce.idBancos import IDBancos

class BancoD(BancoChain):

    def __init__(self):
        super().__init__(IDBancos.bancoD)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco D")
