from musica.ordenador import Ordenador


class PorAutor(Ordenador):
    """
    Ordena as músicas por autor
    """

    def vem_antes(self, musica1, musica2):
        """
        Verifica se o autor da musica1 vem antes do autor da musica dois
        ou se os autores são iguais
        """

        if (musica1.nome >= musica2.nome):
            return True
        else:
            return False
