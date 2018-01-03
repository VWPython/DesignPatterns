from mensagens.emissor import Emissor


class Email(Emissor):
    """
    Emissor de email.
    """

    def envia(self, mensagem):
        print("Enviando por Email a mensagem:", mensagem)
