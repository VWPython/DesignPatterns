from dados.observadores.tabela import Tabela
from dados.observadores.porcento import Porcento
from dados.subject import Subject
from dados.dados import Dados


def main():
    """
    Função principal
    """

    dados = Subject()
    dados.adiciona_observador(Tabela(dados))
    dados.adiciona_observador(Porcento(dados))

    dados.modifica_estado(Dados(7, 3, 1))
    dados.modifica_estado(Dados(2, 3, 1))


if __name__ == '__main__':
    main()
