from pagamentos.emissor import Emissor
from pagamentos.receptor import Receptor


class EmissorVisa(Emissor):
    """
    Emissor Visa
    """

    def envia(self, mensagem):
        """
        Envia mensagens para a Visa.
        """

        print("Enviando a seguinte mensagem para a Visa:", mensagem)


class ReceptorVisa(Receptor):
    """
    Receptor Visa.
    """

    def recebe(self):
        """
        Recebe mensagens da Visa.
        """

        print("Recebendo mensagem da Visa.")
        mensagem = "Mensagem da visa"
        return mensagem
