from processo_seletivo.concursos import Marinha, Aeronautica


def main():
    """
    Quanto temos diferentes algoritmos que possuem estruturas parecidas.

    Ele tem uma estrutura parecida com às linhas de montagem de carro,
    pois permite definir a ordem de execução dos passos que resolvem um
    determinado problema e permite que cada passo possa ser implementado
    de maneiras diferentes.
    """

    concurso = Marinha()
    concurso.executa()

    print("\n")

    concurso = Aeronautica()
    concurso.executa()


if __name__ == '__main__':
    main()
