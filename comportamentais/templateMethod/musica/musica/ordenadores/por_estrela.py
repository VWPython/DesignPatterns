from musica.ordenador import Ordenador


class PorEstrela(Ordenador):
    """
    Ordena as músicas por estrelas.
    """

    def vem_antes(self, musica1, musica2):
        """
        Verifica se a musica1 tem uma quantidade de estrelas maior
        que a musica2
        """

        if (musica1.estrelas > musica2.estrelas):
            return True
        else:
            return False
