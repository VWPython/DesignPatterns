from sistema.subsistemas import SistemaDeAudio, SistemaDeVideo, SistemaDeInput


class SistemaFacade(object):
    """
    Sistema Facade - sistema de subsistemas.
    """

    sistema_de_video = None
    sistema_de_audio = None
    sistema_de_input = None

    def inicializar_subsistemas(self):
        """
        Inicializa todos os subsistemas e suas configurações.
        """

        self.sistema_de_video = SistemaDeVideo()
        self.sistema_de_video.configurar_cores()
        self.sistema_de_video.configurar_resolucao()

        self.sistema_de_input = SistemaDeInput()
        self.sistema_de_input.configurar_joystick()
        self.sistema_de_input.configurar_teclado()

        self.sistema_de_audio = SistemaDeAudio()
        self.sistema_de_audio.configurar_canais()
        self.sistema_de_audio.configurar_frequencia()
        self.sistema_de_audio.configurar_volume()

    def reproduzir_audio(self, arquivo):
        """
        Reproduzir audio do subsistema de audio
        """

        self.sistema_de_audio.reproduzir_audio(arquivo)

    def renderizar_imagem(self, imagem):
        """
        Reproduzir imagem do subsistema de video.
        """

        self.sistema_de_video.renderizar_imagem(imagem)

    def ler_input(self):
        """
        Ler entradas e saídas do subsistema de input.
        """

        self.sistema_de_input.ler_input()
