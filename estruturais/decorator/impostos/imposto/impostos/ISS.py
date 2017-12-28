from imposto.imposto import Imposto
from imposto.decorator import IPVX


class ISS(Imposto):
    """
    Imposto ISS.
    """

    @IPVX
    def calcula(self, orcamento):
        """
        Calcula o imposto ISS.
        """

        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)
