from configuracoes.configuracao import Configuracao


def main():
    configuracao = Configuracao.pega_instancia()
    print(configuracao.pega_propriedade("time-zone"))
    print(configuracao.pega_propriedade("currency-code"))
    print(configuracao.pega_propriedade("language"))

if __name__ == '__main__':
    main()
