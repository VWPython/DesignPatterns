from abc import ABC, abstractmethod

class CalculaImposto(ABC):

    @abstractmethod
    def calcula_salario_com_imposto(funcionario):
        pass
