from mensagens.fabrica_de_emissores import FabricaDeEmissores


def main():
    """
    Encapsula a escolha da classe concreta a ser utilizada na criação de
    objetos de um determinado tipo

    A fábrica (interface) cria objetos que só serão definidos em tempo de
    execução pela suas subclasses
    """

    fabrica = FabricaDeEmissores()

    emissor = fabrica.cria_emissor(FabricaDeEmissores.SMS)
    emissor.envia("K19 - Treinamentos")

    emissor = fabrica.cria_emissor(FabricaDeEmissores.EMAIL)
    emissor.envia("K19 - Treinamentos")

    emissor = fabrica.cria_emissor(FabricaDeEmissores.JMS)
    emissor.envia("K19 - Treinamentos")


if __name__ == '__main__':
    main()
