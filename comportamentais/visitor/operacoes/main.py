from operacoes.simples import Soma, Subtracao, Multiplicacao, Divisao
from operacoes.impressao import Impressora
from operacoes.numero import Numero


def main():
    """
    Função principal.
    NÃO TA FUNCIONANDO.
    """

    impressao = Impressora()

    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Subtracao(Numero(5), Numero(2))
    expressao_esquerda = Soma(expressao_esquerda, expressao_direita)
    resultado = Soma(expressao_esquerda, Numero(7))
    dividendo = Multiplicacao(resultado, Numero(2))

    resultado = Divisao(dividendo, Numero(0))
    resultado.executa()

    resultado = Divisao(dividendo, Numero(10))

    resultado.aceita(impressao)

    print("{0} = {1}".format(
        resultado.aceita(impressao),
        resultado.executa()
    ))


if __name__ == '__main__':
    main()
