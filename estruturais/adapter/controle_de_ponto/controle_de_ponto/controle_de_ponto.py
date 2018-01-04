from controle_de_ponto.antigo import ControleDePonto as ControleDePontoAntigo
from controle_de_ponto.novo import ControleDePonto as ControleDePontoNovo


class ControleDePonto(ControleDePontoAntigo):
    """
    Adaptador para o novo controle de ponto.
    """

    def __init__(self):
        """
        Constroi o adaptador.
        """

        self.controle_de_ponto = ControleDePontoNovo()

    def registra_entrada(self, funcionario):
        """
        Registra a entrada de um funcionario.
        """

        self.controle_de_ponto.registra(funcionario)

    def registra_saida(self, funcionario):
        """
        Registra a saída de um funcionario.
        """

        self.controle_de_ponto.registra(funcionario, entrada=False)
