from operacoes.simples import Soma, Subtracao, Multiplicacao, Divisao
from operacores import Impressora, Numero


def main():
    """
    Quando temos uma árvore, e precisamos navegar nessa árvore de maneira
    organizada, podemos usar um Visitor

    Permitir atualizações específicas em uma coleção de objetos de acordo
    com o tipo particular de cada objeto atualizado.

    Representar uma operação a ser executada nos elementos de uma
    estrutura de objetos. Visitor permite definir uma nova operação
    sem mudar as classes dos elementos sobre os quais opera.
    """

    impressao = Impressora()

    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Subtracao(Numero(5), Numero(2))
    expressao_esquerda = Soma(expressao_esquerda, expressao_direita)
    resultado = Soma(expressao_esquerda, Numero(7))
    dividendo = Multiplicacao(resultado, Numero(2))

    resultado = Divisao(dividendo, Numero(10))

    print("{0} = {1}".format(
        resultado.aceita(impressao),
        resultado.executa()
    ))


if __name__ == '__main__':
    main()
