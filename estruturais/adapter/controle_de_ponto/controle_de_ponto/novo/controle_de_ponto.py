from datetime import datetime


class ControleDePonto(object):
    """
    Controle de ponto antigo.
    """

    def registra(self, funcionario, entrada=True):
        """
        Registra a entrada ou a saída do funcionario.
        """

        time = datetime.today()

        if entrada is True:
            print("Entrada: %s às %2.2d:%2.2d" % (
                funcionario.nome, time.hour, time.minute
            ))
        else:
            print("Saída: %s às %2.2d:%2.2d" % (
                funcionario.nome, time.hour, time.minute
            ))
