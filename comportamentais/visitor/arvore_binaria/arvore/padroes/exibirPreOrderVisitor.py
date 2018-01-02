from arvore.arvoreVisitante import ArvoreVisitante


class ExibirPreOrderVisitor(ArvoreVisitante):
    """
    Visita os elementos da arvoré de busca pré-ordem.

                        A
                       / \
                      B   D
                     /   / \
                    C   E   F
    """

    def visitar(self, no):
        """
        Visitar primeiro a raiz, depois a sub-árvore esquerda e por
        último a sub-árvore direita.

        Percorre: ABCDEF
        """

        if (no is None):
            return

        print(no)

        self.visitar(no.esquerda)

        self.visitar(no.direita)
