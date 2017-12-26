from canal.canais.canaisEsporte import CanaisEsporte
from canal.canais.canaisFilme import CanaisFilme

def main():
    canais_de_esporte = CanaisEsporte()
    iterador = canais_de_esporte.criar_iterador()
    print("Canais de esporte:")
    while not iterador.is_done():
        print(iterador.current_item())
        iterador.next()

    canais_de_filme = CanaisFilme()
    iterador = canais_de_filme.criar_iterador()
    print("\nCanais de filme:")
    while not iterador.is_done():
        print(iterador.current_item())
        iterador.next()

if __name__ == '__main__':
    main()
