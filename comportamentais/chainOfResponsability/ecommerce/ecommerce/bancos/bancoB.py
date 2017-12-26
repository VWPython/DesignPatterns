from ecommerce.bancoChain import BancoChain
from ecommerce.idBancos import IDBancos

class BancoB(BancoChain):

    def __init__(self):
        super().__init__(IDBancos.bancoB)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco B")
