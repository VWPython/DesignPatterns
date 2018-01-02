from abc import ABC, abstractmethod


class Ordenador(ABC):
    """
    Classe abstrata responsavel por ordenar as músicas.
    """

    @abstractmethod
    def vem_antes(self, musica1, musica2):
        """
        Verifica qual a musica que vem antes.
        """

        pass

    def ordenar_musica(self, lista):
        """
        Ordena as músicas
        """

        nova_lista = []

        for musicaMP3 in lista:
            nova_lista.append(musicaMP3)

        for i in range(len(nova_lista)):
            for j in range(i, len(nova_lista)):
                if (not self.vem_antes(nova_lista[i], nova_lista[j])):
                    temporaria = nova_lista.index(nova_lista[j])
                    nova_lista[j] = nova_lista[i]
                    nova_lista[i] = nova_lista[temporaria]

        return nova_lista
