from musica.ordenadorTemplate import OrdenadorTemplate

class OrdenadorPorAutor(OrdenadorTemplate):

    def is_primeiro(self, musica1, musica2):
        if (musica1.nome >= musica2.nome):
            return True
        else:
            return False
