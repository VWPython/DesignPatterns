from editor.texto import Texto


def main():
    """
    Função principal
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
