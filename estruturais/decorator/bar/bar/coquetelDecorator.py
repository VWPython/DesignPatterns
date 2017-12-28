from bar.coquetel import Coquetel


class CoquetelDecorator(Coquetel):

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel dinamicamente.
        """

        self.coquetel = coquetel

    def get_nome(self):
        """
        Pega o nome do coquetel e insere junto com o nome do adicional.
        """

        return self.coquetel.get_nome() + " + " + self.nome

    def get_preco(self):
        """
        Pega o preço do coquetel e soma com o do preço do adicional.
        """

        return self.coquetel.get_preco() + self.preco
