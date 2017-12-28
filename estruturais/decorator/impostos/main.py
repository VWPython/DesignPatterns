from imposto.impostos.ISS import ISS
from imposto.impostos.ICMS import ICMS
from imposto.calculador import CalculadorDeImpostos
from imposto.orcamento import Orcamento


def main():
    """
    Função principal.
    """

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)

    calculador.realize_calculo(orcamento, ISS())
    calculador.realize_calculo(orcamento, ICMS())
    calculador.realize_calculo(orcamento, ISS(ICMS()))
    calculador.realize_calculo(orcamento, ISS(ICMS(ISS())))


if __name__ == '__main__':
    main()
