from pagamentos.emissor import Emissor
from pagamentos.receptor import Receptor


class EmissorMasterCard(Emissor):
    """
    Emissor MasterCard
    """

    def envia(self, mensagem):
        """
        Envia a mensagem para o mastercard
        """

        print("Enviando a seguinte mensagem para o MasterCard:", mensagem)


class ReceptorMasterCard(Receptor):
    """
    Receptor MasterCard
    """

    def recebe(self):
        """
        Recebe mensagens do MasterCard
        """

        print("Recebendo mensagem do MasterCard.")
        mensagem = "Mensagem do mastercard"
        return mensagem
