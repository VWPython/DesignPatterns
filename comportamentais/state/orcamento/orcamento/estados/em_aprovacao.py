from orcamento.estado import EstadoDoOrcamento
from orcamento.estados.aprovado import Aprovado
from orcamento.estados.reprovado import Reprovado


class EmAprovacao(EstadoDoOrcamento):
    """
    Classe responsavel por verificar se o estado do orçamento
    está em aprovação
    """

    def aplica_desconto_extra(self, orcamento):
        """
        Aplica desconto extra se o orçamento estive no estado
        de aprovação
        """

        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.total * 0.02)
            self.desconto_aplicado = True
        else:
            print("Desconto já foi aplicado.")

    def aprova(self, orcamento):
        """
        Aprova o orçamento atual.
        """

        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        """
        Reprova o orçamento atual
        """

        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        """
        Finaliza o orçamento atual
        """

        print("Orçamentos em aprovação não podem ser finalizados.")
