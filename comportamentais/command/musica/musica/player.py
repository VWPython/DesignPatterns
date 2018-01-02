class Player(object):
    """
    Tocador de música.
    """

    def play(self, arquivo):
        """
        Toca a música.
        """

        print("Tocando a musica:", arquivo)

    def aumentar_volume(self, intensidade):
        """
        Aumenta o volume do player
        """

        print("Aumentando o volume em", intensidade, "níveis")

    def diminuir_volume(self, intensidade):
        """
        Diminui o volume do player
        """

        print("Diminuindo o volume em", intensidade, "níveis")
