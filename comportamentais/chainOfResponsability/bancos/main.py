from banco.bancos.bancoA import BancoA
from banco.bancos.bancoB import BancoB
from banco.bancos.bancoC import BancoC
from banco.bancos.bancoD import BancoD
from banco.idBancos import IDBancos


def main():

    lista_de_bancos = BancoA()
    lista_de_bancos.insere(BancoB())
    lista_de_bancos.insere(BancoC())
    lista_de_bancos.insere(BancoD())

    try:
        lista_de_bancos.efetua_pagamento(IDBancos.bancoC)
        lista_de_bancos.efetua_pagamento(IDBancos.bancoD)
        lista_de_bancos.efetua_pagamento(IDBancos.bancoA)
        lista_de_bancos.efetua_pagamento(IDBancos.bancoB)
    except NameError:
        raise


if __name__ == '__main__':
    main()
