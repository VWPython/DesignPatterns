from abc import ABC, abstractmethod


class CalculaImposto(ABC):
    """
    Class abstrata responsavel pela implementação dos impostos
    """

    @abstractmethod
    def calcula_salario_com_imposto(funcionario):
        """
        Calcula o salario com o imposto especifico do funcionario.
        """

        pass
