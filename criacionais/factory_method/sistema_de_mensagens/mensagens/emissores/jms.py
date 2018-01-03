from mensagens.emissor import Emissor


class JMS(Emissor):
    """
    Emissor de JMS
    """

    def envia(self, mensagem):
        print("Enviando por JMS a mensagem:", mensagem)
