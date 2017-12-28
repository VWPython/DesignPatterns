from orcamento.estado import EstadoDoOrcamento


class Finalizado(EstadoDoOrcamento):
    """
    Classe responsavel por verificar se o estado do orçamento
    está finalizado
    """

    def aplica_desconto_extra(self, orcamento):
        """
        Orçamento finalizado não tem disconto
        """

        print("Orçamentos finalizados não recebem desconto extra.")

    def aprova(self, orcamento):
        """
        Aprova o orçamento atual.
        """

        print("Orçamento já finalizado.")

    def reprova(self, orcamento):
        """
        Reprova o orçamento atual
        """

        print("Orçamento já finalizado.")

    def finaliza(self, orcamento):
        """
        Finaliza o orçamento atual
        """

        print("Orçamento já finalizado.")
