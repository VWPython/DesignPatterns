from editor import Texto


def main():
    """
    Sem violar o encapsulamento, capturar e externalizar um estado interno
    de um objeto, de maneira que o objeto possa ser restaurado para esse
    estado mais tarde.
    """

    texto = Texto()
    texto.escreve_texto("Primeira linha do texto\n")
    texto.escreve_texto("Segunda linha do texto\n")
    texto.escreve_texto("Terceira linha do texto\n")
    texto.mostra_texto()
    texto.desfaze_escrita()
    texto.mostra_texto()
    texto.desfaze_escrita()
    texto.mostra_texto()
    texto.desfaze_escrita()
    texto.mostra_texto()
    texto.desfaze_escrita()
    texto.mostra_texto()


if __name__ == '__main__':
    main()
