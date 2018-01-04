from janela.janelaImplementada import JanelaImplementada


class JanelaWindows(JanelaImplementada):
    """
    Janela do Windows.
    """

    def desenha_janela(self, titulo):
        """
        Desenha a janela.
        """

        print(titulo + " - Janela windows")

    def desenha_botao(self, titulo):
        """
        Desenha o botão da janela do windows.
        """

        print(titulo + " - Botão windows")
