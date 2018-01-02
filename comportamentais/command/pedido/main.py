from pedidos.comandos import Concluir, Pagar
from pedidos import Pedido, FilaDeTrabalho


def main():
    """
    Função principal.
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
