from banco.bancos import BancoA, BancoB, BancoC, BancoD
from banco.idBancos import IDBancos


def main():
    """
    Função principal
    """

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
