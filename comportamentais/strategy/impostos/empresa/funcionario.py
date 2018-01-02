from empresa.impostos.calculaImpostoQuinzeOuDez import CalculaImpostoQuinzeOuDez
from empresa.impostos.calculaImpostoVinteOuQuinze import CalculaImpostoVinteOuQuinze


class Funcionario(object):
    """
    Classe responsavel pelo funcionario.
    """

    DESENVOLVEDOR = 1
    GERENTE = 2
    DBA = 3

    def __init__(self, cargo, salario_base):
        """
        Cria o funcionario passando o cargo que ele desempenha e o salario
        base dele para que se possa inserir o imposto adequado.
        """

        self.__salario_base = salario_base

        if (cargo == self.DESENVOLVEDOR):
            self.estrategia_de_calculo = CalculaImpostoQuinzeOuDez()
            self.cargo = self.DESENVOLVEDOR

        elif (cargo == self.DBA):
            self.estrategia_de_calculo = CalculaImpostoQuinzeOuDez()
            self.cargo = self.DBA

        elif (cargo == self.GERENTE):
            self.estrategia_de_calculo = CalculaImpostoVinteOuQuinze()
            self.cargo = self.GERENTE

        else:
            raise NameError("Cargo não encontrado!")

    def calcula_salario_com_imposto(self):
        """
        Calcula o salario do funcionario de acordo com seu cargo
        """

        return self.estrategia_de_calculo.calcula_salario_com_imposto(self)

    @property
    def salario_base(self):
        """
        Pega o salario base do funcionario.
        """

        return self.__salario_base
