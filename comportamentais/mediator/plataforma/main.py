from plataforma import MensagemMediator
from plataforma.plataformas import IOS, Android


def main():
    """
    Quando uma situação em que um relacionamento muitos para muitos é
    necessário, uma boa prática é criar uma tabela intermediária e deixar
    que ela relaciona uma entidade com outras várias e vice versa.

    É semelhante a central telefônica, pois diminui a quantidade de ligações
    entre objetos introduzindo um mediador, através da qual toda comunicação
    entre os objetos será realizada, ou seja, eliminar conexões excessivas
    entre elementos por meio da introdução de um intermediário único.
    """

    mediator = MensagemMediator()

    android = Android(mediator)
    ios = IOS(mediator)

    mediator.adiciona(android)
    mediator.adiciona(ios)

    android.envia_mensagem("Oi, eu sou o android")
    ios.envia_mensagem("Olá android, eu sou o IOS")


if __name__ == '__main__':
    main()
