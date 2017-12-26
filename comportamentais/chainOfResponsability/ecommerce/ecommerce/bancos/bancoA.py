from ecommerce.bancoChain import BancoChain
from ecommerce.idBancos import IDBancos

class BancoA(BancoChain):

    def __init__(self):
        super().__init__(IDBancos.bancoA)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco A")
