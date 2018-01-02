from plataforma.mediator import Mediator
from plataforma.plataformas.ios import IOS
from plataforma.plataformas.android import Android


class MensagemMediator(Mediator):
    """
     Implementação particular do Mediador, que coordena a
     interação entre as diferentes plataformas.
    """

    def __init__(self):
        """
        Cria uma lista de contatos que irão receber as mensagens.
        """

        self.contatos = []

    def adiciona(self, plataforma):
        """
        Adiciona os colegas na lista de contatos.
        """

        self.contatos.append(plataforma)

    def envia(self, mensagem, plataforma):
        """
        Envia a mensagem a alguma plataforma.
        """

        for contato in self.contatos:
            if (contato != plataforma):
                self.__definir_protocolo(contato)
                contato.recebe_mensagem(mensagem)

    def __definir_protocolo(self, contato):
        """
        Define o protocolo de envio de mensagem para plataformas
        IOS ou Android
        """

        if (type(contato) == type(IOS)):
            print("Protocolo IOS")
        elif (type(contato) == type(Android)):
            print("Protocolo Android")
