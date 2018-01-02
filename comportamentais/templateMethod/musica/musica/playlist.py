from musica.ordenadores import PorAutor, PorEstrela, PorNome, PorAno
from musica.modo_de_reproducao import ModoDeReproducao
from musica.musicaMP3 import MusicaMP3


class Playlist(object):
    """
    Playlist de músicas.
    """

    musicas = []
    ordenador = None

    def __init__(self, modo_de_reproducao=ModoDeReproducao.porNome):
        """
        Modo de reprodução da playlist de músicas.
        """

        if (modo_de_reproducao == ModoDeReproducao.porAno):
            self.ordenador = PorAno()
        elif (modo_de_reproducao == ModoDeReproducao.porAutor):
            self.ordenador = PorAutor()
        elif (modo_de_reproducao == ModoDeReproducao.porEstrela):
            self.ordenador = PorEstrela()
        elif (modo_de_reproducao == ModoDeReproducao.porNome):
            self.ordenador = PorNome()
        else:
            self.ordenador = PorNome()
            print("Opção padrão: ordenado por nome")

    def modifica_modo_de_reproducao(self, modo_de_reproducao=ModoDeReproducao.porNome):
        """
        Modifica o modo de reprodução da playlist.
        """

        if (modo_de_reproducao == ModoDeReproducao.porAno):
            self.ordenador = PorAno()
        elif (modo_de_reproducao == ModoDeReproducao.porAutor):
            self.ordenador = PorAutor()
        elif (modo_de_reproducao == ModoDeReproducao.porEstrela):
            self.ordenador = PorEstrela()
        elif (modo_de_reproducao == ModoDeReproducao.porNome):
            self.ordenador = PorNome()
        else:
            self.ordenador = PorNome()
            print("Opção padrão: ordenado por nome")

    def adicionar_musica(self, nome, autor, ano, estrela):
        """
        Adicionar música.
        """

        self.musicas.append(MusicaMP3(nome, autor, ano, estrela))

    def mostrar_lista_de_reproducao(self):
        """
        Mostra a lista de reprodução.
        """

        nova_lista = []
        nova_lista = self.ordenador.ordenar_musica(self.musicas)

        for musica in nova_lista:
            print("{0} - {1}\nAno: {2}\nEstrelas: {3}\n".format(
                musica.nome,
                musica.autor,
                musica.ano,
                musica.estrelas
            ))
