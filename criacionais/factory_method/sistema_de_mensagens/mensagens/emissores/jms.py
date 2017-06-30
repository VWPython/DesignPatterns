from mensagens.emissor import Emissor


class JMS(Emissor):

    def envia(self, mensagem):
        print("Enviando por JMS a mensagem:", mensagem)
