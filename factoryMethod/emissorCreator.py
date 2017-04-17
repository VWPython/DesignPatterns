from emissorJMS import EmissorJMS
from emissorSMS import EmissorSMS
from emissorEmail import EmissorEmail

class EmissorCreator(object):
    SMS = 0
    EMAIL = 1
    JMS = 2

    def create(self, tipo_de_emissor):
        if(tipo_de_emissor == self.SMS):
            return EmissorSMS()
        elif(tipo_de_emissor == self.EMAIL):
            return EmissorEmail()
        elif(tipo_de_emissor == self.JMS):
            return EmissorJMS()
        else:
            raise NameError("Tipo de emissor não suportado")
