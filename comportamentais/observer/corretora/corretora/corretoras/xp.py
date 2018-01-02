from corretora.corretora import Observador


class XP(Observador):
    """
    Corretora XP que irá observar as ações da bolsa de valores
    """

    def notifica_alteracao(self, acao):
        """
        Notificar alterações nas ações da bolsa.
        """

        print("Corretora XP sendo notificada.")
        print("A ação", acao.codigo, "teve o seu valor alterado para", acao.valor)
