from arvore.no import No


class ArvoreBinaria(object):
    """
    Arvore binária de busca.
    """

    def __init__(self, chave_raiz):
        """
        Constroi a arvore binária de busca.
        """

        self.raiz = No(chave_raiz)
        self.quantidade_de_elementos = 0

    def inserir(self, chave):
        """
        Insere elementos dentro da arvore.
        """

        self.__insere(chave, self.raiz)

    def remover(self, chave):
        """
        Remove elementos da arvore.
        """

        pass

    def buscar(self, chave):
        """
        Busca elemento na arvore
        """

        pass

    def __insere(self, chave, no):
        """
        Insere um elemento na arvore passando a chave e o nó especifico.
        """

        if (no.chave == chave):
            return

        if (chave > no.chave):
            if (no.direita is None):
                no.direita = No(chave)
                self.quantidade_de_elementos += 1
                return
            self.__insere(chave, no.direita)
        else:
            if (no.esquerda is None):
                no.esquerda = No(chave)
                self.quantidade_de_elementos += 1
                return
            self.__insere(chave, no.esquerda)

    def aceitar_visitante(self, visitante):
        """
        Aceita a visita de um visitante na arvore de busca.
        """

        visitante.visitar(self.raiz)
