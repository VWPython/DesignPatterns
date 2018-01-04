from janela.janelaImplementada import JanelaImplementada


class JanelaLinux(JanelaImplementada):
    """
    Janela do Linux
    """

    def desenha_janela(self, titulo):
        """
        Desenha a janela do linux.
        """

        print(titulo + " - Janela linux")

    def desenha_botao(self, titulo):
        """
        Desenha o botão da janela do linux.
        """

        print(titulo + " - Botão linux")
