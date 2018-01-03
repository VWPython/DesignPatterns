from temas import Tema


def main():
    """
    Permitir a criação de uma quantidade limitada de instâncias de
    determinada classe e fornecer um modo para recuperá-las.
    """

    tema_fire1 = Tema.pega_instancia(Tema.FIRE)
    print("Tema: %s" % tema_fire1.nome)
    print("Cor da fonte: %s" % tema_fire1.cor_da_fonte)
    print("Cor de fundo: %s" % tema_fire1.cor_de_fundo)

    tema_fire2 = Tema.pega_instancia(Tema.FIRE)
    print("---------------------")
    print("Comparando as referências")
    print("Tema fire1 é igual ao tema fire2:", tema_fire1 == tema_fire2)
    print("---------------------")


if __name__ == '__main__':
    main()
