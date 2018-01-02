from loja.pagamentos import CartaoDeCredito, CartaoDeDebito, Boleto
from loja import Loja


def main():
    """
    Função principal.
    """

    lojas_americanas = Loja("Lojas Americanas")
    lojas_americanas.executa_compra(999.00, CartaoDeCredito())
    lojas_americanas.executa_compra(49.90, Boleto())
    lojas_americanas.executa_compra(99.00, CartaoDeDebito())

    casas_bahia = Loja("Casas Bahia")
    casas_bahia.executa_compra(19.00, CartaoDeCredito())


if __name__ == '__main__':
    main()
