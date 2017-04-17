from emissorCreator import EmissorCreator

creator = EmissorCreator()


emissor = creator.create(EmissorCreator.JMS)
emissor.envia("Mensagem em JMS!")

emissor = creator.create(EmissorCreator.SMS)
emissor.envia("Mensagem em SMS!")

emissor = creator.create(EmissorCreator.EMAIL)
emissor.envia("Mensagem em Email!")
