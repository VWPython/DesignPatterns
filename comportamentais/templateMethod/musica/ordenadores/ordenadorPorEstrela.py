from musica.ordenadorTemplate import OrdenadorTemplate

class OrdenadorPorEstrela(OrdenadorTemplate):

    def is_primeiro(self, musica1, musica2):
        if (musica1.estrelas > musica2.estrelas):
            return True
        else:
            return False
