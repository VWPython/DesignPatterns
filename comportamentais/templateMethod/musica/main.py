from musica.playlist import Playlist
from musica.modo_de_reproducao import ModoDeReproducao


def main():
    """
    Função principal
    BUG: Lógica de ordenação por nome e autor está falhando.
    """

    playlist = Playlist()
    playlist.adicionar_musica("Everlong", "Foo Fighters", 1997, 5)
    playlist.adicionar_musica("Song 2", "Blur", 1997, 4)
    playlist.adicionar_musica("American Jesus", "Bad Religion", 1993, 3)
    playlist.adicionar_musica("No Cigar", "Milencollin", 2001, 2)
    playlist.adicionar_musica("Ten", "Pearl Jam", 1991, 1)

    print("==== Lista por Nome de Musica ====")
    playlist.mostrar_lista_de_reproducao()

    print("\n==== Lista por Autor ====")
    playlist.modifica_modo_de_reproducao(ModoDeReproducao.porAutor)
    playlist.mostrar_lista_de_reproducao()

    print("\n==== Lista por Ano ====")
    playlist.modifica_modo_de_reproducao(ModoDeReproducao.porAno)
    playlist.mostrar_lista_de_reproducao()

    print("\n==== Lista por Estrela ====")
    playlist.modifica_modo_de_reproducao(ModoDeReproducao.porEstrela)
    playlist.mostrar_lista_de_reproducao()


if __name__ == '__main__':
    main()
