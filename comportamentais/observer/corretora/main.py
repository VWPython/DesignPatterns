from corretora import Acao
from corretora.corretoras import HomeBroker, XP


def main():
    """
    Atribui aos objetos que tem seus estados alterados a tarefa de notificar
    os objetos interessados nessas mudanças, por exemplo, Na bolsa de valores
    as ações estão em constante mudança e as corretoras e bancos sempre querem
    ficar observando as alterações nessas ações.
    """

    acao = Acao("Vale3", 45.27)

    home_broker = HomeBroker()
    xp = XP()

    acao.registra_observador(home_broker)
    acao.registra_observador(xp)
    acao.retira_observador(home_broker)

    acao.valor = 50


if __name__ == '__main__':
    main()
