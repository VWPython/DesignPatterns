from imposto.imposto import Imposto
from imposto.decorator import IPVX


class ICMS(Imposto):
    """
    Imposto ICMS.
    """

    @IPVX
    def calcula(self, orcamento):
        """
        Calcula o imposto ISS.
        """

        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)
