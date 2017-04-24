from banco.bancoDeUsuarios import BancoDeUsuarios

class BancoProxy(BancoDeUsuarios):
    usuario = ''
    senha = ''

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def pega_numero_de_usuarios(self):
        if(self.__tem_permissao_de_acesso()):
            return super().pega_numero_de_usuarios()
        return "Só usuário administrador pode acessar o número de usuários"

    def pega_usuarios_conectados(self):
        if(self.__tem_permissao_de_acesso()):
            return super().pega_usuarios_conectados()
        return "Só usuário administrador pode acessar os usuários conectadas"

    def __tem_permissao_de_acesso(self):
        return self.usuario == "admin" and self.senha == "admin"
