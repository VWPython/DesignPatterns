from imagem.adapters import SDLImageAdapter, OpenGLImageAdapter


def main():
    """
    Permite que um objeto seja substituido por outro que, apesar de realizar
    a mesma tarefa, possui uma interface diferente.
    """

    imagem = SDLImageAdapter()
    imagem.carrega_imagem("teste_sdl.png")
    imagem.desenha_imagem(0, 0, 10, 10)

    imagem = OpenGLImageAdapter()
    imagem.carrega_imagem("teste_opengl.png")
    imagem.desenha_imagem(0, 0, 10, 10)


if __name__ == '__main__':
    main()
