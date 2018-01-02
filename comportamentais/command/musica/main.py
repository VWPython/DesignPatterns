from musica import Player, ListaDeComandos
from musica.comandos import Tocar, AumentarVolume, DiminuirVolume


def main():
    """
    Função principal.
    """

    player = Player()
    lista_de_comandos = ListaDeComandos()

    lista_de_comandos.adiciona(Tocar(player, "musica.mp3"))
    lista_de_comandos.adiciona(AumentarVolume(player, 3))
    lista_de_comandos.adiciona(DiminuirVolume(player, 2))

    lista_de_comandos.executa()


if __name__ == '__main__':
    main()
