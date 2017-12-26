from sistema.subsistemas.sistemaDeAudio import SistemaDeAudio
from sistema.subsistemas.sistemaDeVideo import SistemaDeVideo
from sistema.subsistemas.sistemaDeInput import SistemaDeInput

class SistemaFacade(object):

    sistema_de_video = None
    sistema_de_audio = None
    sistema_de_input = None

    def inicializar_subsistemas(self):
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
        self.sistema_de_audio.reproduzir_audio(arquivo)

    def renderizar_imagem(self, imagem):
        self.sistema_de_video.renderizar_imagem(imagem)

    def ler_input(self):
        self.sistema_de_input.ler_input()
