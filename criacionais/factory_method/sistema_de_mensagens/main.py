from mensagens.fabrica_de_emissores import FabricaDeEmissores


def main():
    fabrica = FabricaDeEmissores()

    emissor = fabrica.cria_emissor(FabricaDeEmissores.SMS)
    emissor.envia("K19 - Treinamentos")

    emissor = fabrica.cria_emissor(FabricaDeEmissores.EMAIL)
    emissor.envia("K19 - Treinamentos")

    emissor = fabrica.cria_emissor(FabricaDeEmissores.JMS)
    emissor.envia("K19 - Treinamentos")

if __name__ == '__main__':
    main()
