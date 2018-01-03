from mensagens.emissor import Emissor


class SMS(Emissor):
    """
    Emissor de SMS
    """

    def envia(self, mensagem):
        print("Enviando por SMS a mensagem:", mensagem)
