from banco import BancoProxy


def main():
    """
    Controlar as chamadas a um objeto através de outro objeto de
    mesma interface.

    Esse padrão define um intermediário para controlar o acesso a um
    determinado objeto, podendo adicionar funcionalidades que esse
    objeto não possui
    """

    print("Hacker acessando")
    banco = BancoProxy("hacker", "1234")
    print(banco.numero_de_usuarios)
    print(banco.usuarios_conectados)

    print("\nAdministrador acessando")
    banco = BancoProxy("admin", "admin")
    print(banco.numero_de_usuarios)
    print(banco.usuarios_conectados)


if __name__ == '__main__':
    main()
