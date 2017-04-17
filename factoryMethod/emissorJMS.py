from emissor import Emissor

class EmissorJMS(Emissor):

    def envia(self, mensagem):
        print("Enviando mensagem por JMS: ", end="")
        print(mensagem)
