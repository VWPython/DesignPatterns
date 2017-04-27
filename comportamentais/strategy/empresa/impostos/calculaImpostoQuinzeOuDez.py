from empresa.calculaImposto import CalculaImposto

class CalculaImpostoQuinzeOuDez(CalculaImposto):

    def calcula_salario_com_imposto(self, funcionario):
        if (funcionario.get_salario_base() > 2000):
            return funcionario.get_salario_base() * 0.85
        else:
            return funcionario.get_salario_base() * 0.9
