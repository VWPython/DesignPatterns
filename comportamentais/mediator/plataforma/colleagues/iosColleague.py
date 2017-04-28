from plataforma.colleague import Colleague

class IOSColleague(Colleague):

    def __init__(self, mediator):
        super().__init__(mediator)

    def recebe_mensagem(self, mensagem):
        print("IOS recebeu:", mensagem)
