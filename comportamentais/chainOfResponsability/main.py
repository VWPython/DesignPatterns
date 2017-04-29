from ecommerce.bancos.bancoA import BancoA
from ecommerce.bancos.bancoB import BancoB
from ecommerce.bancos.bancoC import BancoC
from ecommerce.bancos.bancoD import BancoD
from ecommerce.idBancos import IDBancos

def main():

    lista_de_bancos = BancoA()
    lista_de_bancos.modifica_proximo(BancoB())
    lista_de_bancos.modifica_proximo(BancoC())
    lista_de_bancos.modifica_proximo(BancoD())

    try:
        lista_de_bancos.efetua_pagamento(IDBancos.bancoC)
        lista_de_bancos.efetua_pagamento(IDBancos.bancoD)
        lista_de_bancos.efetua_pagamento(IDBancos.bancoA)
        lista_de_bancos.efetua_pagamento(IDBancos.bancoB)
    except NameError:
        raise

if __name__ == '__main__':
    main()
