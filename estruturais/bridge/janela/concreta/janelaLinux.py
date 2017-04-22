from janela.janelaImplementada import JanelaImplementada

class JanelaLinux(JanelaImplementada):

    def desenha_janela(self, titulo):
        print(titulo + " - Janela linux")

    def desenha_botao(self, titulo):
        print(titulo + " - Botão linux")
