from janela.janelaImplementada import JanelaImplementada
from janela.janelaAbstrata import JanelaAbstrata

class JanelaAviso(JanelaAbstrata):

    def __init__(self, janela):
        super().__init__(janela)

    def desenhar(self):
        self.desenha_janela("Janela de Aviso")
        self.desenha_botao("OK")
