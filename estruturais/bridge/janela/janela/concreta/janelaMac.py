from janela.janelaImplementada import JanelaImplementada


class JanelaMac(JanelaImplementada):
    """
    Janela do MAC.
    """

    def desenha_janela(self, titulo):
        """
        Desenha a janela do MAC.
        """

        print(titulo + " - Janela mac")

    def desenha_botao(self, titulo):
        """
        Desenha os botões da janela do MAC
        """

        print(titulo + " - Botão mac")
