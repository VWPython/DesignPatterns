from banco.bancos import BancoA, BancoB, BancoC, BancoD
from banco.idBancos import IDBancos


def main():
    """
    Usado para acabar com estruturas de decisão, evitando o acoplamento
    utilizando uma cadeia de solicitações até que uma trate

    Evitar o acoplamento do remetente de uma solicitação ao seu receptor,
    ao dar a mais de um objeto a oportunidade de tratar a solicitação.
    Encadear os objetos receptores, passando a solicitação ao longo da
    cadeia até que um objeto a trate.
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
