from contratos import Historico, Contrato
from datetime import date


def main():
    """
    Sem violar o encapsulamento, capturar e externalizar um estado interno
    de um objeto, de maneira que o objeto possa ser restaurado para esse
    estado mais tarde.
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
