from abc import ABC, abstractmethod

class JanelaAbstrata(ABC):

    janela = None

    def __init__(self, janela):
        self.janela = janela

    def desenha_janela(self, titulo):
        self.janela.desenha_janela(titulo)

    def desenha_botao(self, titulo):
        self.janela.desenha_botao(titulo)

    @abstractmethod
    def desenhar(self):
        pass
