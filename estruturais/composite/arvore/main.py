from arvore.arquivoComponent import ArquivoComponent
from arvore.arquivoComposite import ArquivoComposite
from arvore.arquivos.arquivoVideo import ArquivoVideo

def main():
    minha_pasta = ArquivoComposite("Minha pasta")
    meu_video = ArquivoVideo("meu video.avi")
    meu_outro_video = ArquivoVideo("serieS01E01.mkv")

    try:
        print("Inserindo arquivos")
        minha_pasta.adiciona(meu_video)
        minha_pasta.adiciona(meu_outro_video)
        minha_pasta.imprime_nome_do_arquivo()
    except NameError:
        raise

    try:
        print("\nPesquisando arquivos:")
        arquivo = minha_pasta.pega_arquivo(meu_video.pega_nome_do_arquivo())
        arquivo.imprime_nome_do_arquivo()
        print("\nRemovendo arquivos:")
        minha_pasta.remove(meu_video.pega_nome_do_arquivo())
        minha_pasta.imprime_nome_do_arquivo()
    except NameError:
        raise

    try:
        print("\nCausando um exception")
        meu_video.adiciona(meu_outro_video)
    except NameError:
        raise

if __name__ == "__main__":
    main()
