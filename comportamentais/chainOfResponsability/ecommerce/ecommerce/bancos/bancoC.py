from ecommerce.bancoChain import BancoChain
from ecommerce.idBancos import IDBancos

class BancoC(BancoChain):

    def __init__(self):
        super().__init__(IDBancos.bancoC)

    def pagar(self):
        print("Pagamento efetuado com sucesso no banco C")
