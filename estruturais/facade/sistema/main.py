from sistema.sistemaFacade import SistemaFacade

def main():
    print("#### Configurando subsistemas ####")
    sistema = SistemaFacade()
    sistema.inicializar_subsistemas()

    print("\n#### Utilizando subsistemas ####")
    sistema.renderizar_imagem("Imagem.png")
    sistema.reproduzir_audio("teste.mp3")
    sistema.ler_input()

if __name__ == '__main__':
    main()
