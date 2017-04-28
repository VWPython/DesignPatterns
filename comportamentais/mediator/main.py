from plataforma.mensagemMediator import MensagemMediator
from plataforma.colleagues.iosColleague import IOSColleague
from plataforma.colleagues.androidColleague import AndroidColleague

def main():

    mediator = MensagemMediator()

    android = AndroidColleague(mediator)
    ios = IOSColleague(mediator)

    mediator.adiciona_colleague(android)
    mediator.adiciona_colleague(ios)

    android.envia_mensagem("Oi, eu sou o android")
    ios.envia_mensagem("Oi, eu sou o IOS")

if __name__ == '__main__':
    main()
