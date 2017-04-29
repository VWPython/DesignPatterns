from arvore.arvoreVisitante import ArvoreVisitante

class ExibirPostOrderVisitor(ArvoreVisitante):

    def visitar(self, no):
        if (no == None):
            return
        self.visitar(no.pega_no_esquerda())
        self.visitar(no.pega_no_direita())
        print(no.to_string())
