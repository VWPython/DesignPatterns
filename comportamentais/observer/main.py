from observador.observadores.tabelaObserver import TabelaObserver
from observador.observadores.porcentoObserver import PorcentoObserver
from observador.dadosSubject import DadosSubject
from observador.dados import Dados

def main():
    dados = DadosSubject()
    dados.adiciona_observador(TabelaObserver(dados))
    dados.adiciona_observador(PorcentoObserver(dados))

    dados.modifica_estado(Dados(7, 3, 1))
    print()
    dados.modifica_estado(Dados(2, 3, 1))

if __name__ == '__main__':
    main()
