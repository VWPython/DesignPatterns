from plataforma.plataforma import Plataforma


class Android(Plataforma):

    def __init__(self, mediator):
        """
        Cria a plataforma Android e passa o mediador que irá cuidar
        da comunicação
        """

        super(Android, self).__init__(mediator)

    def recebe_mensagem(self, mensagem):
        """
        Recebe mensagens através do mediador.
        """

        print("Android recebeu:", mensagem)
