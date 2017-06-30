from recursos.objetos.mesa import MesaCompartilhada


def main():
    mesa_compartilhada = MesaCompartilhada()

    mesa = mesa_compartilhada.adquire(7)
    mesa_compartilhada.libera(7)
    mesa_compartilhada.libera(7)

if __name__ == '__main__':
    main()
