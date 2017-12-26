from empresa.impostos.calculaImpostoQuinzeOuDez import CalculaImpostoQuinzeOuDez
from empresa.impostos.calculaImpostoVinteOuQuinze import CalculaImpostoVinteOuQuinze

class Funcionario(object):

    DESENVOLVEDOR = 1
    GERENTE = 2
    DBA = 3
    salario_base = 0.0
    cargo = 0
    calcula_imposto = None
    estrategia_de_calculo = None

    def __init__(self, cargo, salario_base):
        self.salario_base = salario_base
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
        return self.estrategia_de_calculo.calcula_salario_com_imposto(self)

    def get_salario_base(self):
        return self.salario_base

