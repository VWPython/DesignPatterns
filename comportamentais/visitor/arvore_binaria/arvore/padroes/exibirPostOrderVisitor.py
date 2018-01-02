from arvore.arvoreVisitante import ArvoreVisitante


class ExibirPostOrderVisitor(ArvoreVisitante):
    """
    Visita os elementos da arvoré de busca pós-ordem

                        A
                       / \
                      B   D
                     /   / \
                    C   E   F
    """

    def visitar(self, no):
        """
        Visitar primeiro a sub-árvore esquerda, depois a sub-árvore direita
        e por último a raiz.

        Percorre: CBEFDA
        """

        if (no is None):
            return

        self.visitar(no.esquerda)

        self.visitar(no.direita)

        print(no)
