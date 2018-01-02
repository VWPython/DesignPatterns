from empresa.calculaImposto import CalculaImposto


class CalculaImpostoVinteOuQuinze(CalculaImposto):
    """
    Calcula salario com imposto de 20% ou 15%
    """

    def calcula_salario_com_imposto(self, funcionario):
        """
        Calcula o salario com imposto de 20% se o salario base for
        maior que 3500 e 15% caso contrario.
        """

        if (funcionario.salario_base > 3500):
            return funcionario.salario_base * 0.8
        else:
            return funcionario.salario_base * 0.85
