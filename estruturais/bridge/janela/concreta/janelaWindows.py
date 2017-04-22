from janela.janelaImplementada import JanelaImplementada

class JanelaWindows(JanelaImplementada):

    def desenha_janela(self, titulo):
        print(titulo + " - Janela windows")

    def desenha_botao(self, titulo):
        print(titulo + " - Botão windows")
