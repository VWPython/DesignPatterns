from romanos.gramaticas import (
    QuatroDigitosRomanos, TresDigitosRomanos,
    DoisDigitosRomanos, UmDigitoRomano
)
from romanos.contexto import Contexto
from romanos.interpretador import Interpretador


def main():

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
