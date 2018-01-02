from plataforma.plataforma import Plataforma


class IOS(Plataforma):

    def __init__(self, mediator):
        """
        Cria a plataforma IOS e passa o mediador que irá cuidar
        da comunicação
        """

        super(IOS, self).__init__(mediator)

    def recebe_mensagem(self, mensagem):
        """
        Recebe mensagens através do mediador.
        """

        print("IOS recebeu:", mensagem)
