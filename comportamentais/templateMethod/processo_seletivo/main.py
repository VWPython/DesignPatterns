from processo_seletivo.concursos import Marinha, Aeronautica


def main():
    """
    Função principal
    """

    concurso = Marinha()
    concurso.executa()

    print("\n")

    concurso = Aeronautica()
    concurso.executa()


if __name__ == '__main__':
    main()
