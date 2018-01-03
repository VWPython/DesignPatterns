from carro.prototipos import PalioPrototipo


def main():
    """
    Função principal
    """

    prototipo_do_palio = PalioPrototipo()

    novo_palio = prototipo_do_palio.clonar()
    novo_palio.valor_da_compra = 27000.0
    novo_palio.exibe_informacao()

    print("")

    palio_usado = novo_palio.clonar()
    palio_usado.exibe_informacao()
    palio_usado.valor_da_compra = 19000.0
    palio_usado.exibe_informacao()


if __name__ == '__main__':
    main()
