from mensagens.emissor import Emissor


class SMS(Emissor):

    def envia(self, mensagem):
        print("Enviando por SMS a mensagem:", mensagem)
