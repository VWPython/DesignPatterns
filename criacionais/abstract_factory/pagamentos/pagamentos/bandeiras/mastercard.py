from pagamentos.emissor import Emissor
from pagamentos.receptor import Receptor


class EmissorMasterCard(Emissor):

    def envia(self, mensagem):
        print("Enviando a seguinte mensagem para o MasterCard:", mensagem)


class ReceptorMasterCard(Receptor):

    def recebe(self):
        print("Recebendo mensagem do MasterCard.")
        mensagem = "Mensagem do mastercard"
        return mensagem
