from mensagens.emissor import Emissor


class Email(Emissor):

    def envia(self, mensagem):
        print("Enviando por Email a mensagem:", mensagem)
