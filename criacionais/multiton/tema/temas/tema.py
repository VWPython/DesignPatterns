class Tema(object):

    temas = {}
    SKY = "Sky"
    FIRE = "Fire"

    # Tem que deixar privado
    def __init__(self):
        self.__nome = ''
        self.__cor_de_fundo = ''
        self.__cor_da_fonte = ''

    @classmethod
    def pega_instancia(self, nome_do_tema):
        if nome_do_tema in Tema.temas:
            return Tema.temas[nome_do_tema]
        else:
            Tema.__constroi_temas()
            return Tema.temas[nome_do_tema]

    @classmethod
    def __constroi_temas(self):
        tema1 = Tema()
        tema1.__nome = Tema.SKY
        tema1.__cor_de_fundo = "Blue"
        tema1.__cor_da_fonte = "Black"

        self.temas[tema1.nome] = tema1

        tema2 = Tema()
        tema2.__nome = Tema.FIRE
        tema2.__cor_de_fundo = "Red"
        tema2.__cor_da_fonte = "White"

        self.temas[tema2.nome] = tema2

    @property
    def nome(self):
        return self.__nome

    @property
    def cor_de_fundo(self):
        return self.__cor_de_fundo

    @property
    def cor_da_fonte(self):
        return self.__cor_da_fonte
