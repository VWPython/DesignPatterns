from romanos.gramaticas import (
    QuatroDigitosRomanos, TresDigitosRomanos,
    DoisDigitosRomanos, UmDigitoRomano
)
from romanos.contexto import Contexto
from romanos.interpretador import Interpretador


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

    numero_romano = "CXCIV"
    contexto = Contexto(numero_romano)

    interpretador = Interpretador()
    interpretador.adicionar_gramatica(QuatroDigitosRomanos())
    interpretador.adicionar_gramatica(TresDigitosRomanos())
    interpretador.adicionar_gramatica(DoisDigitosRomanos())
    interpretador.adicionar_gramatica(UmDigitoRomano())

    interpretador.interpretar(contexto)

    print(numero_romano + " = " + str(contexto.resultado))


if __name__ == '__main__':
    main()
