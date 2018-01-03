from dados import Subject, Dados
from dados.observadores import Tabela, Porcento


def main():
    """
    Atribui aos objetos que tem seus estados alterados a tarefa de notificar
    os objetos interessados nessas mudanças, por exemplo, Na bolsa de valores
    as ações estão em constante mudança e as corretoras e bancos sempre querem
    ficar observando as alterações nessas ações.
    """

    dados = Subject()
    dados.adiciona_observador(Tabela(dados))
    dados.adiciona_observador(Porcento(dados))

    dados.modifica_estado(Dados(7, 3, 1))
    dados.modifica_estado(Dados(2, 3, 1))


if __name__ == '__main__':
    main()
