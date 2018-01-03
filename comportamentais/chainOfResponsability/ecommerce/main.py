from ecommerce import (Calculador, Carrinho, Item)


def main():
    """
    Usado para acabar com estruturas de decisão, evitando o acoplamento
    utilizando uma cadeia de solicitações até que uma trate

    Evitar o acoplamento do remetente de uma solicitação ao seu receptor,
    ao dar a mais de um objeto a oportunidade de tratar a solicitação.
    Encadear os objetos receptores, passando a solicitação ao longo da
    cadeia até que um objeto a trate.
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
