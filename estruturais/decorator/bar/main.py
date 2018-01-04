from bar.bebidas import Cachaca
from bar.adicionais import Acuca, Suco


def main():
    """
    Adiciona funcionalidade a um objeto dinamicamente.
    """

    coquetel = Cachaca()
    print(coquetel.get_nome(), "= R$", str(coquetel.get_preco()))

    coquetel = Suco(coquetel)
    print(coquetel.get_nome(), "= R$", str(coquetel.get_preco()))

    coquetel = Acuca(coquetel)
    print(coquetel.get_nome(), "= R$", str(coquetel.get_preco()))


if __name__ == '__main__':
    main()
