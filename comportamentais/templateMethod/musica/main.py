from musica import Playlist, ModoDeReproducao


def main():
    """
    BUG: Lógica de ordenação por nome e autor está falhando.

    Quanto temos diferentes algoritmos que possuem estruturas parecidas.

    Ele tem uma estrutura parecida com às linhas de montagem de carro,
    pois permite definir a ordem de execução dos passos que resolvem um
    determinado problema e permite que cada passo possa ser implementado
    de maneiras diferentes.
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
