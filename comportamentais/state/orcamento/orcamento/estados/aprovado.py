from orcamento.estado import EstadoDoOrcamento
from orcamento.estados.finalizado import Finalizado


class Aprovado(EstadoDoOrcamento):
    """
    Classe responsavel por verificar se o estado do orçamento
    está aprovado
    """

    def aplica_desconto_extra(self, orcamento):
        """
        Aplica desconto extra se o orçamento estive no estado aprovado.
        """

        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.total * 0.05)
            self.desconto_aplicado = True
        else:
            print("Desconto já foi aplicado.")

    def aprova(self, orcamento):
        """
        Aprova o orçamento atual.
        """

        print("O orçamento já está aprovado.")

    def reprova(self, orcamento):
        """
        Reprova o orçamento atual
        """

        print("O orçamento já está aprovado, não pode ser reprovado.")

    def finaliza(self, orcamento):
        """
        Finaliza o orçamento atual
        """

        orcamento.estado_atual = Finalizado()
