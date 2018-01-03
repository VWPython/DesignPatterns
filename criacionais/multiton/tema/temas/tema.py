class Tema(object):
    """
    Tema multiton
    """

    temas = {}
    SKY = "Sky"
    FIRE = "Fire"

    # Instancia privada do tema.
    __instancia = False

    def __init__(self):
        """
        Construtor do tema, se o tema já existir apenas mostre a mensagem.
        """

        if self.__instancia:
            raise ValueError("O objeto já existe! utilize a função pega_instancia()")

        self.__nome = ''
        self.__cor_de_fundo = ''
        self.__cor_da_fonte = ''

    @classmethod
    def pega_instancia(self, nome_do_tema):
        """
        Pega as instâncias dos temas criados ou cria elas.
        """

        if nome_do_tema in Tema.temas:
            return Tema.temas[nome_do_tema]
        else:
            Tema.__constroi_temas()
            return Tema.temas[nome_do_tema]

    @classmethod
    def __constroi_temas(self):
        """
        Constroi os temas.
        """

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

        self.__intancia = True

    @property
    def nome(self):
        """
        Pega o nome do tema.
        """

        return self.__nome

    @property
    def cor_de_fundo(self):
        """
        Pega a cor de fundo do tema.
        """

        return self.__cor_de_fundo

    @property
    def cor_da_fonte(self):
        """
        Pega a cor da fonte do tema.
        """

        return self.__cor_da_fonte
