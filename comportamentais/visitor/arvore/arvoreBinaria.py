from arvore.no import No

class ArvoreBinaria(object):

    def __init__(self, chave_raiz):
        self.raiz = No(chave_raiz)
        self.quantidade_de_elementos = 0

    def inserir(self, chave):
        self.__insere(chave, self.raiz)

    def remover(self, chave):
        pass

    def buscar(self, chave):
        pass

    def __insere(self, chave, no):
        if (no.pega_chave() == chave):
            return

        if (chave > no.pega_chave()):
            if (no.pega_no_direita() == None):
                no.modifica_no_direita(No(chave))
                self.quantidade_de_elementos += 1
                return
            self.__insere(chave, no.pega_no_direita())
        else:
            if (no.pega_no_esquerda() == None):
                no.modifica_no_esquerda(No(chave))
                self.quantidade_de_elementos += 1
                return
            self.__insere(chave, no.pega_no_esquerda())

    def aceitar_visitante(self, visitante):
        visitante.visitar(self.raiz)

