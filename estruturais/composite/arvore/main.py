from arvore import ArquivoComposite
from arvore.arquivos import ArquivoVideo


def main():
    """
    Agrupa objetos que fazem parte de uma relação parte-todo de forma a
    tratá-los sem distinção
    """

    pasta = ArquivoComposite("Minha pasta")
    video1 = ArquivoVideo("meu video.avi")
    video2 = ArquivoVideo("serieS01E01.mkv")

    print("***** Inserindo arquivos *****")
    pasta.adiciona(video1)
    pasta.adiciona(video2)
    pasta.mostra()

    print("\n***** Pesquisando arquivos *****")
    arquivo = pasta.pega(video1.titulo)
    arquivo.mostra()

    print("\n****** Removendo arquivos *****")
    pasta.remove(video1.titulo)
    pasta.mostra()

    print("\n****** Causando um exception *****")
    video1.adiciona(video2)


if __name__ == "__main__":
    main()
