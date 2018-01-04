from sistema import SistemaFacade


def main():
    """
    Prove uma interface simplificada para a utilização de várias
    interfaces de um subsistema.

    A ideia do Facade é a mesma da agência de viagem, ou seja,
    simplificar a interação de um cliente com diversos sistemas,
    por exemplo, compnhias aéreas, hotéis, e etc...
    """

    print("***** Configurando subsistemas *****")
    sistema = SistemaFacade()
    sistema.inicializar_subsistemas()

    print("\n***** Utilizando subsistemas *****")
    sistema.renderizar_imagem("Imagem.png")
    sistema.reproduzir_audio("teste.mp3")
    sistema.ler_input()


if __name__ == '__main__':
    main()
