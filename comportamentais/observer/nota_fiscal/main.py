from compras.observadores import envia_por_email, imprime, salva_no_banco
from compras import Item, NotaFiscal


def main():
    """
    Atribui aos objetos que tem seus estados alterados a tarefa de notificar
    os objetos interessados nessas mudanças, por exemplo, Na bolsa de valores
    as ações estão em constante mudança e as corretoras e bancos sempre querem
    ficar observando as alterações nessas ações.
    """

    itens = [
        Item('Item A', 100),
        Item('Item B', 200)
    ]

    nota_fiscal = NotaFiscal(
        razao_social="FHSA Limitada",
        cnpj="0123445569705",
        itens=itens,
        observadores=[imprime, envia_por_email, salva_no_banco]
    )


if __name__ == '__main__':
    main()
