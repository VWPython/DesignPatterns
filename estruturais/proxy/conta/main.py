from conta import Conta, ContaProxy


def main():
    """
    Controlar as chamadas a um objeto através de outro objeto de mesma
    interface.

    Esse padrão define um intermediário para controlar o acesso a um
    determinado objeto, podendo adicionar funcionalidades que esse
    objeto não possui
    """

    conta = Conta()
    conta_proxy = ContaProxy(conta)

    conta_proxy.deposita(500)
    print("Saldo:", conta_proxy.saldo)

    conta_proxy.saca(59)
    print("Saldo:", conta_proxy.saldo)


if __name__ == '__main__':
    main()
