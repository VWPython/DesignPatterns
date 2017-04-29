from arvore.arvoreVisitante import ArvoreVisitante

class ExibirPreOrderVisitor(ArvoreVisitante):

    def visitar(self, no):
        if (no == None):
            return
        print(no.to_string())
        self.visitar(no.pega_no_esquerda())
        self.visitar(no.pega_no_direita())
