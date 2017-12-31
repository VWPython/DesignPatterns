class Divisao(object):
    """
    Operação simples de divisao.
    """

    def __init__(self, dividendo, divisor):
        """
        Constroi a operação simples de divisao passando a expressão do lado
        esquerdo e a expressão do lado direito.
        """

        self.__dividendo = dividendo
        self.__divisor = divisor

    @property
    def resto(self):
        """
        Pega o resto da divisão.
        """

        return self.__dividendo % self.__divisor

    def executa(self):
        """
        Retorna a divisao das duas expressões: esquerda e direita.
        """

        try:
            quociente = self.__dividendo.executa() / self.__divisor.executa()
        except ZeroDivisionError:
            print("Não se pode dividir por zero.")
        else:
            return quociente
