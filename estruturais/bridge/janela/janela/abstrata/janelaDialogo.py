from janela.janelaAbstrata import JanelaAbstrata


class JanelaDialogo(JanelaAbstrata):
    """
    Janela de dialógo.
    """

    def __init__(self, janela):
        """
        Cria a janela de dialogo.
        """

        super().__init__(janela)

    def desenhar(self):
        """
        Desenha a janela de dialogo.
        """

        self.desenha_janela("Janela de Diálogo")
        self.desenha_botao("Botão sim")
        self.desenha_botao("Botão não")
        self.desenha_botao("Botão Cancelar")
