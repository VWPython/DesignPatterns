from abc import ABC, abstractmethod


class JanelaImplementada(ABC):
    """
    Classe abstrata que serve como base para criar janelas concretas,
    ou seja, janela do windows, linux, e etc...
    """

    @abstractmethod
    def desenha_janela(self, titulo):
        """
        Desenha a janela.
        """

        pass

    @abstractmethod
    def desenha_botao(self, titulo):
        """
        Desenha os botões.
        """

        pass
