from carro import FabricaDeCarros


def main():
    """
    Permitir a criação de uma única instância de uma classe e fornecer um
    modo para recuperá-la.
    """

    fabrica = FabricaDeCarros.pega_instancia()
    fabrica.cria_carro_fiat()
    fabrica.cria_carro_ford()
    fabrica.cria_carro_volks()
    fabrica.gera_relatorio()

    print("Segunda instancia")
    fabrica = FabricaDeCarros.pega_instancia()
    fabrica.gera_relatorio()


if __name__ == '__main__':
    main()
