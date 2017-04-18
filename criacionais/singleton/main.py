from carro.fabricaDeCarros import FabricaDeCarros

def main():
    fabrica = FabricaDeCarros.pega_instancia()
    fabrica.cria_carro_fiat()
    fabrica.cria_carro_ford()
    fabrica.cria_carro_volks()
    fabrica.gera_relatorio()

    fabrica = FabricaDeCarros.pega_instancia()
    fabrica.gera_relatorio()

if __name__ == '__main__':
    main()
