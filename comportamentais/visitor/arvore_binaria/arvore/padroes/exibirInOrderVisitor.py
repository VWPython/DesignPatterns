from arvore.arvoreVisitante import ArvoreVisitante


class ExibirInOrderVisitor(ArvoreVisitante):
    """
    Exibe a arvore binária de busca em-ordem.

                        A
                       / \
                      B   D
                     /   / \
                    C   E   F
    """

    def visitar(self, no):
        """
        Visita primeiro a raiz, depois a sub-árvore esquerda e
        por último a sub-árvore direita.

        Percorre: CBAEDF
        """

        if (no is None):
            return

        self.visitar(no.esquerda)

        print(no)

        self.visitar(no.direita)
