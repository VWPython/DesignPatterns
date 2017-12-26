from abc import ABC, abstractmethod

class JanelaImplementada(ABC):

    @abstractmethod
    def desenha_janela(self, titulo):
        pass

    @abstractmethod
    def desenha_botao(self, titulo):
        pass
