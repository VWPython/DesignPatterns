from abc import ABC, abstractmethod


class Plataforma(ABC):
    """
    Possível interface para padronizar as plataformas de comunicação.
    """

    def __init__(self, mediator):
        """
        Cria a plataforma passando o mediador
        """

        self.mediator = mediator

    def envia_mensagem(self, mensagem):
        """
        Envia a mensagem para o plataforma especifica.
        """

        self.mediator.envia(mensagem, self)

    @abstractmethod
    def recebe_mensagem(self, mensagem):
        """
        Recebe mensagem de alguma plataforma.
        """

        pass
