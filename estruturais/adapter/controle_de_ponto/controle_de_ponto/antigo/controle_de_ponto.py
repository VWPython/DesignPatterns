from datetime import datetime


class ControleDePonto(object):
    """
    Controle de ponto antigo.
    """

    def registra_entrada(self, funcionario):
        """
        Registra a entrada do funcionario.
        """

        time = datetime.today()

        print("Entrada: {0} às {1}:{2}:{3}".format(
            funcionario.nome,
            time.hour,
            time.minute,
            time.second
        ))

    def registra_saida(self, funcionario):
        """
        Registra a saida do funcionario.
        """

        time = datetime.today()

        print("Saída: {0} às {1}:{2}:{3}".format(
            funcionario.nome,
            time.hour,
            time.minute,
            time.second
        ))
