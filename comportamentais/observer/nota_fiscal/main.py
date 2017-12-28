from compras.item import Item
from compras.nota_fiscal import NotaFiscal
from compras.observadores.envia import envia_por_email
from compras.observadores.imprime import imprime
from compras.observadores.salva import salva_no_banco


def main():
    """
    Função principal.
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
