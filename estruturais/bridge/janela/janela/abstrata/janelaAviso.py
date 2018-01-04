from janela.janelaAbstrata import JanelaAbstrata


class JanelaAviso(JanelaAbstrata):
    """
    Janela de aviso.
    """

    def __init__(self, janela):
        """
        Cria a janela de aviso.
        """

        super().__init__(janela)

    def desenhar(self):
        """
        Desenha a janela de aviso.
        """

        self.desenha_janela("Janela de Aviso")
        self.desenha_botao("OK")
