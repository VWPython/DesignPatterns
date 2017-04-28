from abc import ABC, abstractmethod

class OrdenadorTemplate(ABC):

    @abstractmethod
    def is_primeiro(self, musica1, musica2):
        pass

    def ordenar_musica(self, lista):
        nova_lista = []

        for musicaMP3 in lista:
            nova_lista.append(musicaMP3)

        for i in range(len(nova_lista)):
            for j in range(i, len(nova_lista)):
                if (not self.is_primeiro(nova_lista[i], nova_lista[j])):
                    temporaria = nova_lista.index(nova_lista[j])
                    nova_lista[j] = nova_lista[i]
                    nova_lista[i] = nova_lista[temporaria]

        return nova_lista
