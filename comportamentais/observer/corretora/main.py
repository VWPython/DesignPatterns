from corretora import Acao
from corretora.corretoras import HomeBroker, XP


def main():
    """
    Função principal
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
