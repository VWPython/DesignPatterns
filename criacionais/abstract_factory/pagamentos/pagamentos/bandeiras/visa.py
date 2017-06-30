from pagamentos.emissor import Emissor
from pagamentos.receptor import Receptor


class EmissorVisa(Emissor):

    def envia(self, mensagem):
        print("Enviando a seguinte mensagem para a Visa:", mensagem)


class ReceptorVisa(Receptor):

    def recebe(self):
        print("Recebendo mensagem da Visa.")
        mensagem = "Mensagem da visa"
        return mensagem
