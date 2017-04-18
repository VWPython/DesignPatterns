from carro.prototipos.palioPrototipo import PalioPrototipo

def main():
    prototipo_do_palio = PalioPrototipo()

    novo_palio = prototipo_do_palio.clonar()
    novo_palio.valor_da_compra = 27000.0

    palio_usado = prototipo_do_palio.clonar()
    palio_usado.valor_da_compra = 19000.0

    novo_palio.exibe_informacao()
    print()
    palio_usado.exibe_informacao()

if __name__ == '__main__':
    main()
