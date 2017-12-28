from orcamento.estado import EstadoDoOrcamento
from orcamento.estados.finalizado import Finalizado


class Reprovado(EstadoDoOrcamento):
    """
    Classe responsavel por verificar se o estado do orçamento
    está reprovado
    """

    def aplica_desconto_extra(self, orcamento):
        """
        Orçamentos reprovados não recebem desconto extra.
        """

        print("Orçamentos reprovados não recebem desconto extra.")

    def aprova(self, orcamento):
        """
        Aprova o orçamento atual.
        """

        print("Orçamento já está reprovado, não pode ser aprovado.")

    def reprova(self, orcamento):
        """
        Reprova o orçamento atual
        """

        print("O orçamento já está reprovado, não pode ser reprovado novamente.")

    def finaliza(self, orcamento):
        """
        Finaliza o orçamento atual
        """

        orcamento.estado_atual = Finalizado()
