from mensagens.emissores import SMS, JMS, Email


class FabricaDeEmissores(object):
    """
    Fabrica de emissores.
    """

    SMS = 0
    EMAIL = 1
    JMS = 2

    def cria_emissor(self, emissor):
        """
        Cria o emissor.
        """

        if emissor == self.SMS:
            return SMS()
        elif emissor == self.EMAIL:
            return Email()
        elif emissor == self.JMS:
            return JMS()
        else:
            raise Exception("Tipo de emissor não suportado")
