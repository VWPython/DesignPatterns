from musica.ordenador import Ordenador


class PorNome(Ordenador):
    """
    Ordena as músicas por nome.
    """

    def vem_antes(self, musica1, musica2):
        """
        Verifica se o nome da musica1 vem antes do nome da musica2
        ou se os nomes são iguais
        """

        if (musica1.nome >= musica2.nome):
            return True
        return False
