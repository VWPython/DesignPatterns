from abc import ABC, abstractmethod


class GramaticaDeNumerosRomanos(ABC):
    """
    Interpreta o número romano
    """

    def interpretar(self, contexto):
        """
        Dicionário de números romanos para interpretação
        """

        if (len(contexto.numero_romano) == 0):
            return

        # Os valores nove e quatro são os únicos que possuem duas
        # casas, ex: IV, IX
        if (contexto.numero_romano.startswith(self.nove())):
            self.__adicionar_ao_resultado(contexto, 9)
            self.__consumir_duas_casas(contexto)
        elif (contexto.numero_romano.startswith(self.quatro())):
            self.__adicionar_ao_resultado(contexto, 4)
            self.__consumir_duas_casas(contexto)
        elif (contexto.numero_romano.startswith(self.cinco())):
            self.__adicionar_ao_resultado(contexto, 5)
            self.__consumir_uma_casa(contexto)

        # Os valores de um são os únicos que repetem, ex: III, CCC, MMM
        while (contexto.numero_romano.startswith(self.um())):
            self.__adicionar_ao_resultado(contexto, 1)
            self.__consumir_uma_casa(contexto)

    def __consumir_uma_casa(self, contexto):
        """
        Consome uma casa do número romano: CXCIV -> XCIV
        """

        contexto.numero_romano = contexto.numero_romano[1:]

    def __consumir_duas_casas(self, contexto):
        """
        Consome duas casas do número romano: CXCIV -> CIV
        """

        contexto.numero_romano = contexto.numero_romano[2:]

    def __adicionar_ao_resultado(self, contexto, numero):
        """
        Adiciona o resultado em número decimal
        """

        contexto.resultado += (numero * self.multiplicador())

    @abstractmethod
    def um(self):
        """
        Número Romano 1: I
        """

        pass

    @abstractmethod
    def quatro(self):
        """
        Número Romano 4: IV
        """

        pass

    @abstractmethod
    def cinco(self):
        """
        Número Romano 5: V
        """

        pass

    @abstractmethod
    def nove(self):
        """
        Número Romano 9: IX
        """

        pass

    @abstractmethod
    def multiplicador(self):
        """
        Multiplica de acordo com o digito passado:
            Um digito: 1
            Dois digitos: 10
            Três digitos: 100
            Quatro digitos: 1000
            ...
        """

        pass
