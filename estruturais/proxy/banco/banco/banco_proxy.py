from banco.banco_de_usuarios import BancoDeUsuarios


class BancoProxy(BancoDeUsuarios):
    """
    Proxy que controla o banco de usuários.
    """

    def __init__(self, usuario, senha):
        """
        Autenticação.
        """

        self.usuario = usuario
        self.senha = senha

    @property
    def numero_de_usuarios(self):
        """
        Pega o número de usuário.
        """

        if(self.__tem_permissao_de_acesso()):
            return super(BancoProxy, self).numero_de_usuarios

        return "Só usuário administrador pode acessar o número de usuários"

    @property
    def usuarios_conectados(self):
        """
        Pega a quantidade de usuários conectados.
        """

        if(self.__tem_permissao_de_acesso()):
            return super(BancoProxy, self).usuarios_conectados

        return "Só usuário administrador pode acessar os usuários conectadas"

    def __tem_permissao_de_acesso(self):
        """
        Verifica se o usuário e senha estão corretos
        """

        return self.usuario == "admin" and self.senha == "admin"
