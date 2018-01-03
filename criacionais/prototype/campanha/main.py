from campanhas.campanha import Campanha


def main():
    """
    Função principal
    """

    nome = "K19"
    vencimento = "21/08/2023"

    campanha = Campanha(nome, vencimento)
    campanha.imprime()

    campanha_clone = campanha.clone()
    campanha_clone.imprime()


if __name__ == '__main__':
    main()
