from bar.bebidas.cachaca import Cachaca
from bar.bebidas.vodka import Vodka
from bar.bebidas.rum import Rum
from bar.adicionais.refrigerante import Refrigerante
from bar.adicionais.acuca import Acuca
from bar.adicionais.suco import Suco
from bar.adicionais.limao import Limao

def main():
    coquetel = Cachaca()
    print(coquetel.get_nome() + " = " + str(coquetel.get_preco()))

    coquetel = Suco(coquetel)
    print(coquetel.get_nome() + " = " + str(coquetel.get_preco()))

    coquetel = Acuca(coquetel)
    print(coquetel.get_nome() + " = " + str(coquetel.get_preco()))

if __name__ == '__main__':
    main()
