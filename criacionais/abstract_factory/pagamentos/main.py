from pagamentos.fabricas.fabrica_de_comunicadores import (
    FabricaDeComunicadoresVisa, FabricaDeComunicadoresMasterCard
)


def main():
    """
    Função principal
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
