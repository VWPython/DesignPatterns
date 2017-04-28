from musica.ordenadores.ordenadorPorAno import OrdenadorPorAno
from musica.ordenadores.ordenadorPorNome import OrdenadorPorNome
from musica.ordenadores.ordenadorPorEstrela import OrdenadorPorEstrela
from musica.ordenadores.ordenadorPorAutor import OrdenadorPorAutor
from musica.modoDeReproducao import ModoDeReproducao
from musica.musicaMP3 import MusicaMP3

class Playlist(object):
    musicas = []
    ordenador = None

    def __init__(self, modo_de_reproducao=ModoDeReproducao.porNome):
        if (modo_de_reproducao == ModoDeReproducao.porAno):
            self.ordenador = OrdenadorPorAno()
        elif (modo_de_reproducao == ModoDeReproducao.porAutor):
            self.ordenador = OrdenadorPorAutor()
        elif (modo_de_reproducao == ModoDeReproducao.porEstrela):
            self.ordenador = OrdenadorPorEstrela()
        elif (modo_de_reproducao == ModoDeReproducao.porNome):
            self.ordenador = OrdenadorPorNome()
        else:
            self.ordenador = OrdenadorPorNome()
            print("Opção padrão: ordenado por nome")

    def modifica_modo_de_reproducao(self, modo_de_reproducao=ModoDeReproducao.porNome):
        if (modo_de_reproducao == ModoDeReproducao.porAno):
            self.ordenador = OrdenadorPorAno()
        elif (modo_de_reproducao == ModoDeReproducao.porAutor):
            self.ordenador = OrdenadorPorAutor()
        elif (modo_de_reproducao == ModoDeReproducao.porEstrela):
            self.ordenador = OrdenadorPorEstrela()
        elif (modo_de_reproducao == ModoDeReproducao.porNome):
            self.ordenador = OrdenadorPorNome()
        else:
            self.ordenador = OrdenadorPorNome()
            print("Opção padrão: ordenado por nome")

    def adicionar_musica(self, nome, autor, ano, estrela):
        self.musicas.append(MusicaMP3(nome, autor, ano, estrela))

    def mostrar_lista_de_reproducao(self):
        nova_lista = []
        nova_lista = self.ordenador.ordenar_musica(self.musicas)

        for musica in nova_lista:
            print(musica.nome + " - " + musica.autor + "\nAno: " + str(musica.ano) + "\nEstrelas: " + str(musica.estrelas))

