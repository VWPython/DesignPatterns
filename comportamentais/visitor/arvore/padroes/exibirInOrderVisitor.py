from arvore.arvoreVisitante import ArvoreVisitante

class ExibirInOrderVisitor(ArvoreVisitante):

    def visitar(self, no):
        if (no == None):
            return
        self.visitar(no.pega_no_esquerda())
        print(no.to_string())
        self.visitar(no.pega_no_direita())
