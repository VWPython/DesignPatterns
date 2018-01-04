from controle_de_ponto import ControleDePonto, Funcionario
import time


def main():
    """
    Permite que um objeto seja substituido por outro que, apesar de realizar
    a mesma tarefa, possui uma interface diferente.
    """

    controle_de_ponto = ControleDePonto()
    funcionario = Funcionario("Marcelo Adnet")
    controle_de_ponto.registra_entrada(funcionario)

    # Dorme 5 segundos
    time.sleep(5)

    controle_de_ponto.registra_saida(funcionario)


if __name__ == '__main__':
    main()
