from arvore.padroes.exibirInOrderVisitor import ExibirInOrderVisitor
from arvore.padroes.exibirPostOrderVisitor import ExibirPostOrderVisitor
from arvore.padroes.exibirPreOrderVisitor import ExibirPreOrderVisitor
from arvore.arvoreBinaria import ArvoreBinaria

def main():
    arvore = ArvoreBinaria(7)

    arvore.inserir(15)
    arvore.inserir(10)
    arvore.inserir(5)
    arvore.inserir(2)
    arvore.inserir(1)
    arvore.inserir(20)

    print("=== Exibindo em ordem ===")
    arvore.aceitar_visitante(ExibirInOrderVisitor())
    print("\n=== Exibindo pre ordem ===")
    arvore.aceitar_visitante(ExibirPreOrderVisitor())
    print("\n=== Exibindo pós ordem ===")
    arvore.aceitar_visitante(ExibirPostOrderVisitor())

if __name__ == '__main__':
    main()
