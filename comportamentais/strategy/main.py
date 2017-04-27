from empresa.funcionario import Funcionario

def main():
    funcionario1 = Funcionario(Funcionario.DESENVOLVEDOR, 2100)
    print(funcionario1.calcula_salario_com_imposto())

    funcionario2 = Funcionario(Funcionario.DESENVOLVEDOR, 1700)
    print(funcionario2.calcula_salario_com_imposto())

    funcionario3 = Funcionario(Funcionario.GERENTE, 1700)
    print(funcionario3.calcula_salario_com_imposto())

if __name__ == '__main__':
    main()
