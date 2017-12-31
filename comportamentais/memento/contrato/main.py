from contratos.historico import Historico
from contratos.contrato import Contrato
from datetime import date


def main():
    """
    Função principal
    """

    historico = Historico()

    contrato = Contrato(
        data=date.today(),
        cliente='Flávio Almenida',
        status='NOVO'
    )

    contrato.executa()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.executa()
    contrato.cliente = 'Romulo Henrique'
    historico.adiciona_estado(contrato.salva_estado())

    contrato.executa()
    historico.adiciona_estado(contrato.salva_estado())

    print("Status do contrato:", contrato.status)
    print("Cliente:", contrato.cliente)

    contrato.restaurar_estado(historico.obtem_estado(0))

    print("\nEstado do contrato restaurado.\n")

    print("Status do contrato:", contrato.status)
    print("Cliente:", contrato.cliente)


if __name__ == '__main__':
    main()
