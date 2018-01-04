from janela.concreta import JanelaMac, JanelaLinux, JanelaWindows
from janela.abstrata import JanelaDialogo, JanelaAviso


def main():
    """
    Separar uma abstração de sua representação, de forma que ambos possam
    variar e produzir tipos de objetos diferentes.

    Por exemplo, a possibilidade de combinar os cartões SIM e os
    aparelhos celulares de forma independente é a característica principal
    proposta pelo padrão Bridge.
    """

    janela = JanelaDialogo(JanelaLinux())
    janela.desenhar()
    print()

    janela = JanelaAviso(JanelaLinux())
    janela.desenhar()
    print()

    janela = JanelaDialogo(JanelaWindows())
    janela.desenhar()
    print()

    janela = JanelaAviso(JanelaMac())
    janela.desenhar()


if __name__ == '__main__':
    main()
