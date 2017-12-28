"""
1. Decoretor receber como parâmetro a função que será adicionado.

2. Empacote o método com o wrapper passando como parâmetro os mesmo
parâmetros passados para calcular, junto com o self para identificar
seu contexto.

3. Podemos aplicar N decorators na função calcula, porém ela ficará
para sempre na função, diferente do decoretor criado nesse DesignPattern
que será inserido dinamicamente em tempo de execução.
"""


def IPVX(calcula):
    """
    Impost IPVX - chama o método ou função de cálculo do imposto ISS ou
    ICMS (calcula) e pega o resultado e soma com R$ 50,00
    """

    def wrapper(self, orcamento):
        """
        Empacota o método calcular e quando o calculo do imposto estiver
        pronto, será acrescido de R$ 50 reais.
        """

        return calcula(self, orcamento) + 50.0

    return wrapper
