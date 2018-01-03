from boleto_bancario.fabricas import FabricaDeBBBoleto
from boleto_bancario import GeradorDeBoleto


def main():
    """
    Função principal
    """

    fabrica_de_boleto = FabricaDeBBBoleto()
    gerador = GeradorDeBoleto(fabrica_de_boleto)
    boleto = gerador.gera_boleto(
        sacado="Marcelo Martins",
        cedente="K19 Treinamentos",
        valor=100.53,
        vencimento="21/08/2010",
        numero=12345675
    )
    boleto.imprime()


if __name__ == '__main__':
    main()
