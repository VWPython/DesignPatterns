from empresa.calculaImposto import CalculaImposto

class CalculaImpostoVinteOuQuinze(CalculaImposto):

    def calcula_salario_com_imposto(self, funcionario):
        if (funcionario.get_salario_base() > 3500):
            return funcionario.get_salario_base() * 0.8
        else:
            return funcionario.get_salario_base() * 0.85
