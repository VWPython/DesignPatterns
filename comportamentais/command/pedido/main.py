from pedidos.comandos import Concluir, Pagar
from pedidos import Pedido, FilaDeTrabalho


def main():
    """
    Controlar as chamadas a um determinado componente, modelando cada
    requisição como um objeto. Permitir que as operações possam ser
    desfeitas, enfileiradas ou registradas através de comandos.

    A ideia do Command é abstrair um comando que deve ser executado, pois não
    é possível executá-lo naquele momento (pois precisamos por em uma fila
    ou coisa do tipo).
    """

    pedido1 = Pedido('Flavio', 200)
    pedido2 = Pedido('Almeida', 400)

    fila_de_trabalho = FilaDeTrabalho()

    comando1 = Concluir(pedido1)
    comando2 = Pagar(pedido1)
    comando3 = Concluir(pedido2)

    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()


if __name__ == '__main__':
    main()
