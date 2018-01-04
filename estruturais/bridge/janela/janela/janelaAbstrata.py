from abc import ABC, abstractmethod


class JanelaAbstrata(ABC):
    """
    Classe abstrata para a criação de janelas abstratas, ou seja,
    janelas de dialogo, de aviso e entre outras.
    """

    janela = None

    def __init__(self, janela):
        """
        Cria a janela.
        """

        self.janela = janela

    def desenha_janela(self, titulo):
        """
        Desenha a janela.
        """

        self.janela.desenha_janela(titulo)

    def desenha_botao(self, titulo):
        """
        Desenha os botões da janela.
        """

        self.janela.desenha_botao(titulo)

    @abstractmethod
    def desenhar(self):
        """
        Desenhar janela.
        """

        pass
