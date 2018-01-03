from pagamentos.fabricas.fabrica_de_comunicadores import (
    FabricaDeComunicadoresVisa, FabricaDeComunicadoresMasterCard
)


def main():
    """
    Fornecer uma interface para criação de famílias de objetos relacionados
    ou dependentes sem especificar suas classes concretas

    Encapsula a escolha da classe concreta a ser utilizada na criação de
    objetos de diversas familias.
    """

    comunicador = FabricaDeComunicadoresVisa()

    transacao = "Valor=550; Senha=123"
    emissor = comunicador.cria_emissor()
    emissor.envia(transacao)

    receptor = comunicador.cria_receptor()
    mensagem = receptor.recebe()
    print(mensagem)

    comunicador = FabricaDeComunicadoresMasterCard()

    transacao = "Valor=220; Senha=321"
    emissor = comunicador.cria_emissor()
    emissor.envia(transacao)

    receptor = comunicador.cria_receptor()
    mensagem = receptor.recebe()
    print(mensagem)


if __name__ == '__main__':
    main()
