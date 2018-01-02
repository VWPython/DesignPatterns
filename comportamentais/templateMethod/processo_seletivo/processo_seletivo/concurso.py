from abc import ABC, abstractmethod


class Concurso(ABC):
    """
    Classe abstrata responsavel pela padronização dos concursos
    """

    @abstractmethod
    def prova_teorica(self):
        """
        Prova teorica do concurso.
        """

        pass

    @abstractmethod
    def prova_pratica(self):
        """
        Prova prática do concurso.
        """

        pass

    @abstractmethod
    def resistencia_fisica(self):
        """
        Prova de resistência física do concurso.
        """

        pass

    @abstractmethod
    def teste_psicologico(self):
        """
        Teste psicologico do concurso.
        """

        pass

    @abstractmethod
    def exame_medico(self):
        """
        Exame médico do concurso.
        """

        pass

    def executa(self):
        """
        Execução de todas as etapas do concurso em ordem.
        """

        self.prova_teorica()
        self.prova_pratica()
        self.teste_psicologico()
        self.exame_medico()
        self.resistencia_fisica()
