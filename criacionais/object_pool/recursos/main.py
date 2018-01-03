from recursos.objetos.mesa import MesaCompartilhada


def main():
    """
    Possibilita o reaproveitamento de objetos

    Uma situação típica em que recursos limitados devem ser reutilizados
    é o do restaurante. O restaurante não adquire novas mesas a medida
    que clientes chegam ao restaurante e as mesas são reutilizadas por
    novos clientes assim que são liberadas.
    """

    mesa_compartilhada = MesaCompartilhada()

    mesa_compartilhada.adquire(7)
    mesa_compartilhada.adquire(7)
    mesa_compartilhada.libera(7)
    mesa_compartilhada.libera(7)


if __name__ == '__main__':
    main()
