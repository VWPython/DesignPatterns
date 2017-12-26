from imagem.adapters.sdlImageAdapter import SDLImageAdapter
from imagem.adapters.openGLImageAdapter import OpenGLImageAdapter

def main():
    imagem = SDLImageAdapter()
    imagem.carrega_imagem("teste_sdl.png")
    imagem.desenha_imagem(0, 0, 10, 10)

    imagem = OpenGLImageAdapter()
    imagem.carrega_imagem("teste_opengl.png")
    imagem.desenha_imagem(0, 0, 10, 10)

if __name__ == '__main__':
    main()
