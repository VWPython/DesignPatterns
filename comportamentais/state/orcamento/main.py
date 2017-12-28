from orcamento.orcamento import Orcamento
from orcamento.item import Item


def main():
    """
    Função principal.
    """

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 01', 100))
    orcamento.adiciona_item(Item('Item 02', 50))
    orcamento.adiciona_item(Item('Item 03', 400))

    print(orcamento.total)
    orcamento.aplica_desconto_extra()
    print(orcamento.total)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(orcamento.total)
    orcamento.finaliza()


if __name__ == '__main__':
    main()
