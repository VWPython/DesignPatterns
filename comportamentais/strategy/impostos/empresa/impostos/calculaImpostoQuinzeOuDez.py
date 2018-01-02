from empresa.calculaImposto import CalculaImposto


class CalculaImpostoQuinzeOuDez(CalculaImposto):
    """
    Calcula o salario com imposto de 15% ou 10%
    """

    def calcula_salario_com_imposto(self, funcionario):
        """
        Calcula o salario com imposto de 15% se o salario base for
        maior que 2000 e 10% caso contrario.
        """

        if (funcionario.salario_base > 2000):
            return funcionario.salario_base * 0.85
        else:
            return funcionario.salario_base * 0.9
