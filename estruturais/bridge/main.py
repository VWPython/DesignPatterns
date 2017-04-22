from janela.abstrata.janelaDialogo import JanelaDialogo
from janela.abstrata.janelaAviso import JanelaAviso
from janela.concreta.janelaWindows import JanelaWindows
from janela.concreta.janelaMac import JanelaMac
from janela.concreta.janelaLinux import JanelaLinux

def main():
    janela = JanelaDialogo(JanelaLinux());
    janela.desenhar();
    print()

    janela = JanelaAviso(JanelaLinux());
    janela.desenhar();
    print()

    janela = JanelaDialogo(JanelaWindows());
    janela.desenhar();
    print()

    janela = JanelaAviso(JanelaMac());
    janela.desenhar();

if __name__ == '__main__':
    main()
