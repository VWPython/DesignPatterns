from mario import Mario


def main():
    """
    Alterar o comportamento de um determinado objeto de acordo com o
    estado no qual ele se encontra, por exemplo, no jogo do mario, ao pegar
    um cogumelo o estado interno do personagem muda e vira um mario grande,
    e ao pegar uma peninha ele aprende a voar, mudando o estado interno
    do personagem.
    """

    mario = Mario()
    mario.pega_cogumelo()
    mario.pega_pena()
    mario.leva_dano()
    mario.pega_flor()
    mario.pega_flor()
    mario.leva_dano()
    mario.leva_dano()
    mario.pega_pena()
    mario.leva_dano()
    mario.leva_dano()
    mario.leva_dano()


if __name__ == '__main__':
    main()
