from banco.bancoProxy import BancoProxy
from banco.bancoDeUsuarios import BancoDeUsuarios

def main():
    banco = BancoDeUsuarios()

    print("Hacker acessando")
    banco = BancoProxy("hacker", "1234")
    print(banco.pega_numero_de_usuarios())
    print(banco.pega_usuarios_conectados())

    print("\nAdministrador acessando")
    banco = BancoProxy("admin", "admin")
    print(banco.pega_numero_de_usuarios())
    print(banco.pega_usuarios_conectados())

if __name__ == '__main__':
    main()
