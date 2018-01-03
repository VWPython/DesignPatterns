from ecommerce import (Calculador, Carrinho, Item)


def main():
    """
    Função principal.
    """

    compra = Carrinho()
    compra.adiciona_item(Item('item01', 100))
    compra.adiciona_item(Item('item02', 100))
    compra.adiciona_item(Item('item03', 100))
    compra.adiciona_item(Item('item04', 100))
    compra.adiciona_item(Item('item05', 100))

    print(compra.valor_total)

    calculador = Calculador()

    desconto = calculador.calcula(compra)

    print('Desconto:', desconto)


if __name__ == '__main__':
    main()
