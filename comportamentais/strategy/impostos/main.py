from empresa.funcionario import Funcionario


def main():
    """
    Função principal
    """

    funcionario1 = Funcionario(Funcionario.DESENVOLVEDOR, 2100)
    print("Salario do desenvolvedor:", funcionario1.calcula_salario_com_imposto())

    funcionario2 = Funcionario(Funcionario.DBA, 1700)
    print("Salario do DBA:", funcionario2.calcula_salario_com_imposto())

    funcionario3 = Funcionario(Funcionario.GERENTE, 1700)
    print("Salario do gerente:", funcionario3.calcula_salario_com_imposto())


if __name__ == '__main__':
    main()
