from bar.coquetel import Coquetel


class CoquetelDecorator(Coquetel):
    """
    Adicional para o coquetel.
    """

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel dinamicamente.
        """

        self.coquetel = coquetel

    def get_nome(self):
        """
        Pega o nome do coquetel e insere junto com o nome do adicional.
        """

        nome = "{0} + {1}".format(self.coquetel.get_nome(), self.nome)

        return nome

    def get_preco(self):
        """
        Pega o preço do coquetel e soma com o do preço do adicional.
        """

        return self.coquetel.get_preco() + self.preco
