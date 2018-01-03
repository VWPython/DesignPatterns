from configuracoes import Configuracao


def main():
    """
    Função principal.
    """

    configuracao = Configuracao.pega_instancia()
    print(configuracao.pega_propriedade("time-zone"))
    print(configuracao.pega_propriedade("currency-code"))
    print(configuracao.pega_propriedade("language"))


if __name__ == '__main__':
    main()
