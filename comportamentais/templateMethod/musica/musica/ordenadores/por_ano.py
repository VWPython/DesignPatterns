from musica.ordenador import Ordenador


class PorAno(Ordenador):
    """
    Ordena as músicas por ano
    """

    def vem_antes(self, musica1, musica2):
        """
        Verifica se o ano da musica1 vem antes do ano da musica2
        """

        if (musica1.ano > musica2.ano):
            return True
        else:
            return False
