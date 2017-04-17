from emissor import Emissor

class EmissorEmail(Emissor):

    def envia(self, mensagem):
        print("Enviando mensagem por Email: ", end="")
        print(mensagem)
