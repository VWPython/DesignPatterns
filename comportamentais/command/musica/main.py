from musica import Player, ListaDeComandos
from musica.comandos import Tocar, AumentarVolume, DiminuirVolume


def main():
    """
    Controlar as chamadas a um determinado componente, modelando cada
    requisição como um objeto. Permitir que as operações possam ser
    desfeitas, enfileiradas ou registradas através de comandos.

    A ideia do Command é abstrair um comando que deve ser executado, pois não
    é possível executá-lo naquele momento (pois precisamos por em uma fila
    ou coisa do tipo).
    """

    player = Player()
    lista_de_comandos = ListaDeComandos()

    lista_de_comandos.adiciona(Tocar(player, "musica.mp3"))
    lista_de_comandos.adiciona(AumentarVolume(player, 3))
    lista_de_comandos.adiciona(DiminuirVolume(player, 2))

    lista_de_comandos.executa()


if __name__ == '__main__':
    main()
