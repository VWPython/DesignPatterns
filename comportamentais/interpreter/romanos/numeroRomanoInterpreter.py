from abc import ABC, abstractmethod

class NumeroRomanoInterpreter(ABC):

    def interpretar(self, contexto):
        if (len(contexto.pega_input()) == 0):
            return

        # Os valores nove e quatro são os únicos que possuem duas casas, ex: IV, IX
        if (contexto.pega_input().startswith(self.nove())):
            self.__adiciona_valor_output(contexto, 9)
            self.__consumir_duas_casas_do_input(contexto)
        elif (contexto.pega_input().startswith(self.quatro())):
            self.__adiciona_valor_output(contexto, 4)
            self.__consumir_duas_casas_do_input(contexto)
        elif (contexto.pega_input().startswith(self.cinco())):
            self.__adiciona_valor_output(contexto, 5)
            self.__consumir_uma_casa_do_input(contexto)

        # Os valores de um são os únicos que repetem, ex: III, CCC, MMM
        while (contexto.pega_input().startswith(self.um())):
            self.__adiciona_valor_output(contexto, 1)
            self.__consumir_uma_casa_do_input(contexto)

    def __consumir_uma_casa_do_input(self, contexto):
        contexto.modifica_input(contexto.pega_input()[:1])

    def __consumir_duas_casas_do_input(self, contexto):
        contexto.modifica_input(contexto.pega_input()[:2])

    def __adiciona_valor_output(self, contexto, numero):
        contexto.modifica_output(contexto.pega_output() + (numero * multiplicador()))

    @abstractmethod
    def um(self):
        pass

    @abstractmethod
    def quatro(self):
        pass

    @abstractmethod
    def cinco(self):
        pass

    @abstractmethod
    def nove(self):
        pass

    @abstractmethod
    def multiplicador(self):
        pass
