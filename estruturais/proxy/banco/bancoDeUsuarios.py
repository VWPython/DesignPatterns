from random import randint

class BancoDeUsuarios(object):
    __quantidade_de_usuarios = 100
    __usuarios_conectados = 35

    def pega_numero_de_usuarios(self):
        return "Total de usuário: " + str(self.__quantidade_de_usuarios)

    def pega_usuarios_conectados(self):
        return "Usuários conectados: " + str(self.__usuarios_conectados)
