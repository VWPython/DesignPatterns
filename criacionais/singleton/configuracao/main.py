from configuracoes import Configuracao


def main():
    """
    Permitir a criação de uma única instância de uma classe e fornecer um
    modo para recuperá-la.
    """

    configuracao = Configuracao.pega_instancia()
    print(configuracao.pega_propriedade("time-zone"))
    print(configuracao.pega_propriedade("currency-code"))
    print(configuracao.pega_propriedade("language"))


if __name__ == '__main__':
    main()
