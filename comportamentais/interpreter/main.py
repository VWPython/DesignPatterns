from romanos.gramatica.quatroDigitosRomanos import QuatroDigitosRomanos
from romanos.gramatica.tresDigitosRomanos import TresDigitosRomanos
from romanos.gramatica.doisDigitosRomanos import DoisDigitosRomanos
from romanos.gramatica.umDigitoRomano import UmDigitoRomano
from romanos.contexto import Contexto

def main():
    interpretadores = []
    interpretadores.append(QuatroDigitosRomanos)
    interpretadores.append(TresDigitosRomanos)
    interpretadores.append(DoisDigitosRomanos)
    interpretadores.append(UmDigitoRomano)

    numero_romano = "CXCIV"
    contexto = Contexto(numero_romano)

    for interpreter in interpretadores:
        interpreter.interpretar(contexto)

    print(numero_romano + " = " + str(contexto.pega_output()))

if __name__ == '__main__':
    main()
