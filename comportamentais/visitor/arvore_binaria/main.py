from arvore import ArvoreBinaria
from arvore.padroes import (
    ExibirInOrderVisitor, ExibirPostOrderVisitor, ExibirPreOrderVisitor
)


def main():
    """
    Quando temos uma árvore, e precisamos navegar nessa árvore de maneira
    organizada, podemos usar um Visitor

    Permitir atualizações específicas em uma coleção de objetos de acordo
    com o tipo particular de cada objeto atualizado.

    Representar uma operação a ser executada nos elementos de uma
    estrutura de objetos. Visitor permite definir uma nova operação
    sem mudar as classes dos elementos sobre os quais opera.
    """

    arvore = ArvoreBinaria(7)

    arvore.inserir(15)
    arvore.inserir(10)
    arvore.inserir(5)
    arvore.inserir(2)
    arvore.inserir(1)
    arvore.inserir(20)

    print("=== Exibindo em ordem ===")
    arvore.aceitar_visitante(ExibirInOrderVisitor())

    print("\n=== Exibindo pré ordem ===")
    arvore.aceitar_visitante(ExibirPreOrderVisitor())

    print("\n=== Exibindo pós ordem ===")
    arvore.aceitar_visitante(ExibirPostOrderVisitor())


if __name__ == '__main__':
    main()
