from abc import ABC, abstractmethod
from bar.coquetel import Coquetel

class CoquetelDecorator(Coquetel):
    coquetel = None

    def __init__(self, coquetel):
        self.coquetel = coquetel

    def get_nome(self):
        return self.coquetel.get_nome() + " + " + self.nome

    def get_preco(self):
        return self.coquetel.get_preco() + self.preco
