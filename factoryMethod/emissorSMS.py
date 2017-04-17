from emissor import Emissor

class EmissorSMS(Emissor):

    def envia(self, mensagem):
        print("Enviando mensagem por SMS: ", end="")
        print(mensagem)
