from janela.janelaImplementada import JanelaImplementada
from janela.janelaAbstrata import JanelaAbstrata

class JanelaDialogo(JanelaAbstrata):

    def __init__(self, janela):
        super().__init__(janela)

    def desenhar(self):
        self.desenha_janela("Janela de Diálogo")
        self.desenha_botao("Botão sim")
        self.desenha_botao("Botão não")
        self.desenha_botao("Botão Cancelar")
