from plataforma.colleague import Colleague

class AndroidColleague(Colleague):

    def __init__(self, mediator):
        super().__init__(mediator)

    def recebe_mensagem(self, mensagem):
        print("Android recebeu:", mensagem)
