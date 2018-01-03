from orcamento import Orcamento, Item


def main():
    """
    Alterar o comportamento de um determinado objeto de acordo com o
    estado no qual ele se encontra, por exemplo, no jogo do mario, ao pegar
    um cogumelo o estado interno do personagem muda e vira um mario grande,
    e ao pegar uma peninha ele aprende a voar, mudando o estado interno
    do personagem.
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
