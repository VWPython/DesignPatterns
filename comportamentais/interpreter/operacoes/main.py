from operacoes.simples import Soma, Subtracao, Multiplicacao, Divisao
from operacoes.numero import Numero


def main():
    """
    Reconhecer padrões é um problema bem complicado, no entanto, quando
    conseguimos formular uma gramática para o problema a solução fica
    bem mais fácil.

    Uma vez definida a grámatica e suas regras, é possível utilizar o
    padrão Interpreter para montar uma estrutura para interpretar os comandos.

    Dada uma linguagem, definir uma representação para sua gramática
    juntamente com um interpretador que usa a representação para interpretar
    sentenças dessa linguagem.
    """

    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Subtracao(Numero(5), Numero(2))
    expressao_esquerda = Soma(expressao_esquerda, expressao_direita)
    resultado = Soma(expressao_esquerda, Numero(7))
    dividendo = Multiplicacao(resultado, Numero(2))

    resultado = Divisao(dividendo, Numero(0))
    resultado.executa()

    resultado = Divisao(dividendo, Numero(10))
    print("Resultado:", resultado.executa())


if __name__ == '__main__':
    main()
