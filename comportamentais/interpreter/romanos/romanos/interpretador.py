class Interpretador(object):
    """
    Interpretador que controi a gramática e retorna o resultado.
    """

    def __init__(self):
        """
        Controi a gramática.
        """

        self.__interpretadores = []

    def interpretar(self, contexto):
        """
        Interpreta os números romanos para decimal
        """

        for interpreter in self.__interpretadores:
            interpreter.interpretar(contexto)

    def adicionar_gramatica(self, gramatica):
        """
        Adiciona uma regra gramatical.
        """

        self.__interpretadores.append(gramatica)
