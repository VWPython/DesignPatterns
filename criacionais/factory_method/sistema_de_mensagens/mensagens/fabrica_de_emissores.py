from mensagens.emissores.sms import SMS
from mensagens.emissores.jms import JMS
from mensagens.emissores.email import Email


class FabricaDeEmissores(object):

    SMS = 0
    EMAIL = 1
    JMS = 2

    def cria_emissor(self, emissor):
        if emissor == self.SMS:
            return SMS()
        elif emissor == self.EMAIL:
            return Email()
        elif emissor == self.JMS:
            return JMS()
        else:
            raise Exception("Tipo de emissor não suportado")
