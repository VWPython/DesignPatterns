from empresa import Funcionario


def main():
    """
    O padrão Strategy é muito útil quando temos um conjunto de algoritmos
    similares, e precisamos alternar entre eles em diferentes pedaços da
    aplicação.

    A ideia fundamental desse padrão é possibilitar facilmente a variação
    do algoritmo a ser utilizado na resolução de um problema
    """

    funcionario1 = Funcionario(Funcionario.DESENVOLVEDOR, 2100)
    print("Salario do desenvolvedor:", funcionario1.calcula_salario_com_imposto())

    funcionario2 = Funcionario(Funcionario.DBA, 1700)
    print("Salario do DBA:", funcionario2.calcula_salario_com_imposto())

    funcionario3 = Funcionario(Funcionario.GERENTE, 1700)
    print("Salario do gerente:", funcionario3.calcula_salario_com_imposto())


if __name__ == '__main__':
    main()
