from musica.ordenadorTemplate import OrdenadorTemplate

class OrdenadorPorAno(OrdenadorTemplate):

    def is_primeiro(self, musica1, musica2):
        if (musica1.ano > musica2.ano):
            return True
        else:
            return False
