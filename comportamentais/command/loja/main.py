from loja.pagamentos import CartaoDeCredito, CartaoDeDebito, Boleto
from loja import Loja


def main():
    """
    Controlar as chamadas a um determinado componente, modelando cada
    requisição como um objeto. Permitir que as operações possam ser
    desfeitas, enfileiradas ou registradas através de comandos.

    A ideia do Command é abstrair um comando que deve ser executado, pois não
    é possível executá-lo naquele momento (pois precisamos por em uma fila
    ou coisa do tipo).
    """

    lojas_americanas = Loja("Lojas Americanas")
    lojas_americanas.executa_compra(999.00, CartaoDeCredito())
    lojas_americanas.executa_compra(49.90, Boleto())
    lojas_americanas.executa_compra(99.00, CartaoDeDebito())

    casas_bahia = Loja("Casas Bahia")
    casas_bahia.executa_compra(19.00, CartaoDeCredito())


if __name__ == '__main__':
    main()
