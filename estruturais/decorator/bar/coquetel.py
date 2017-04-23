from abc import ABC, abstractmethod

class Coquetel(ABC):
    nome = ''
    preco = 0.0

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
