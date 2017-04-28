from plataforma.mediator import Mediator
from plataforma.colleagues.iosColleague import IOSColleague
from plataforma.colleagues.androidColleague import AndroidColleague

class MensagemMediator(Mediator):

    def __init__(self):
        self.contatos = []

    def adiciona_colleague(self, colleague):
        self.contatos.append(colleague)

    def envia(self, mensagem, colleague):
        for contato in self.contatos:
            if (contato != colleague):
                self.__definir_protocolo(contato)
                contato.recebe_mensagem(mensagem)

    def __definir_protocolo(self, contato):
        if (type(contato) == type(IOSColleague)):
            print("Protocolo IOS")
        elif (type(contato) == type(AndroidColleague)):
            print("Protocolo Android")
