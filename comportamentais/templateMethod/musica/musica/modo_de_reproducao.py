from enum import Enum


class ModoDeReproducao(Enum):
    """
    Modo de reprodução das músicas enumerados.
    """

    porNome = 1
    porAutor = 2
    porAno = 3
    porEstrela = 4
