# IMPORTAÇÃO DE MODULOS.
import tkinter
import threading
import logica_jogo_da_velha
from time import sleep
from fontes import *
from cores import *


class jogo_velha(object):
    def __init__(self, mestre):
        self.interface = mestre
        self.minhavez = False
        self.tabuleiro = []
        for linha in range(3):
            self.tabuleiro.append([])
            for coluna in range(3):
                self.tabuleiro[linha].append(0)

        self.interface['bg'] = cinza
        self.interface.title('JOGO DA VELHA')
        self.interface.geometry('1000x600')

        #FRAMES DA INTERFACE.
        self.frame0 = tkinter.Frame(self.interface, bg=cinza)
        self.frame1 = tkinter.Frame(self.interface, bg=cinza)
        self.frame2 = tkinter.Frame(self.interface, bg=cinza)
        self.framel0 = tkinter.Frame(self.frame2, bg=cinza)
        self.framel1 = tkinter.Frame(self.frame2, bg=cinza)
        self.framel2 = tkinter.Frame(self.frame2, bg=cinza)

        #elementos para ajuste da interface.
        self.mensagem = tkinter.Label(self.frame0, bg=cinza, pady=20, font=fonte_mensagem_v)
        self.nada = tkinter.Label(self.frame1, text='', padx=205, bg=cinza)
        self.title = tkinter.Label(self.frame1, text='Jogo da velha', pady=10, bg=cinza, font=fonte_title_v, fg=azul_claro)
        self.t0x0 = tkinter.Button(self.framel0, text='', command=self.c0x0, padx=25, pady=20)
        self.t0x1 = tkinter.Button(self.framel0, text='', command=self.c0x1, padx=25, pady=20)
        self.t0x2 = tkinter.Button(self.framel0, text='', command=self.c0x2, padx=25, pady=20)
        self.t1x0 = tkinter.Button(self.framel1, text='', command=self.c1x0, padx=25, pady=20)
        self.t1x1 = tkinter.Button(self.framel1, text='', command=self.c1x1, padx=25, pady=20)
        self.t1x2 = tkinter.Button(self.framel1, text='', command=self.c1x2, padx=25, pady=20)
        self.t2x0 = tkinter.Button(self.framel2, text='', command=self.c2x0, padx=25, pady=20)
        self.t2x1 = tkinter.Button(self.framel2, text='', command=self.c2x1, padx=25, pady=20)
        self.t2x2 = tkinter.Button(self.framel2, text='', command=self.c2x2, padx=25, pady=20)
        self.denovo = tkinter.Button(self.interface, text='NOVO JOGO', command=self.novo_jogo, padx=1000, font=fonte_sair, fg=verde_fosco)

        self.mensagem['text'] = 'Faça uma jogada:'
        self.mensagem['fg'] = 'green'

        self.mostra_jogo()

    def mostra_jogo(self):
        self.denovo.pack()
        self.frame0.pack()
        self.mensagem.pack()
        self.frame1.pack(side=tkinter.LEFT)
        self.frame2.pack(side=tkinter.LEFT)
        self.framel0.pack()
        self.framel1.pack()
        self.framel2.pack()

        # elementos para ajuste da interface.
        self.title.pack()
        self.nada.pack()
        self.t0x0.pack(side=tkinter.LEFT)
        self.t0x1.pack(side=tkinter.LEFT)
        self.t0x2.pack(side=tkinter.LEFT)
        self.t1x0.pack(side=tkinter.LEFT)
        self.t1x1.pack(side=tkinter.LEFT)
        self.t1x2.pack(side=tkinter.LEFT)
        self.t2x0.pack(side=tkinter.LEFT)
        self.t2x1.pack(side=tkinter.LEFT)
        self.t2x2.pack(side=tkinter.LEFT)

    def fazer_jogada(self):
        results = logica_jogo_da_velha.resultado(self.tabuleiro)
        if not results:
            self.mensagem['text'] = 'Calculando'
            self.mensagem['fg'] = amarelo_fosco
            sleep(0.1)
            self.mensagem['text'] = 'Calculando.'
            sleep(0.1)
            self.mensagem['text'] = 'Calculando..'
            sleep(0.1)
            self.mensagem['text'] = 'Calculando...'
            sleep(0.2)
            self.mensagem['text'] = 'Sua vez:'
            self.mensagem['fg'] = 'green'
            jogada = logica_jogo_da_velha.jogar(self.tabuleiro)
            self.tabuleiro[jogada[0]][jogada[1]] = -1
            if jogada == [0, 0]:
                self.t0x0['bg'] = vermelho_fosco
            elif jogada == [0, 1]:
                self.t0x1['bg'] = vermelho_fosco
            elif jogada == [0, 2]:
                self.t0x2['bg'] = vermelho_fosco
            elif jogada == [1, 0]:
                self.t1x0['bg'] = vermelho_fosco
            elif jogada == [1, 1]:
                self.t1x1['bg'] = vermelho_fosco
            elif jogada == [1, 2]:
                self.t1x2['bg'] = vermelho_fosco
            elif jogada == [2, 0]:
                self.t2x0['bg'] = vermelho_fosco
            elif jogada == [2, 1]:
                self.t2x1['bg'] = vermelho_fosco
            elif jogada == [2, 2]:
                self.t2x2['bg'] = vermelho_fosco
            self.minhavez = False
        results = logica_jogo_da_velha.resultado(self.tabuleiro)
        if results != False:
            self.minhavez = True
            if results == 'perdi':
                self.mensagem['text'] = 'Parabens, voce venceu!!'
                self.mensagem['fg'] = 'green'
            elif results == 'ganhei':
                self.mensagem['text'] = 'você perdeu!'
                self.mensagem['fg'] = 'red'
            elif results == 'cheio':
                self.mensagem['text'] = 'Empatou.'
                self.mensagem['fg'] = 'white'

    def c0x0(self):
        if not self.minhavez:
            if self.t0x0['bg'] == 'SystemButtonFace':
                self.t0x0['bg'] = verde_fosco
                self.tabuleiro[0][0] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c0x1(self):
        if not self.minhavez:
            if self.t0x1['bg'] == 'SystemButtonFace':
                self.t0x1['bg'] = verde_fosco
                self.tabuleiro[0][1] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c0x2(self):
        if not self.minhavez:
            if self.t0x2['bg'] == 'SystemButtonFace':
                self.t0x2['bg'] = verde_fosco
                self.tabuleiro[0][2] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c1x0(self):
        if not self.minhavez:
            if self.t1x0['bg'] == 'SystemButtonFace':
                self.t1x0['bg'] = verde_fosco
                self.tabuleiro[1][0] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c1x1(self):
        if not self.minhavez:
            if self.t1x1['bg'] == 'SystemButtonFace':
                self.t1x1['bg'] = verde_fosco
                self.tabuleiro[1][1] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c1x2(self):
        if not self.minhavez:
            if self.t1x2['bg'] == 'SystemButtonFace':
                self.t1x2['bg'] = verde_fosco
                self.tabuleiro[1][2] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c2x0(self):
        if not self.minhavez:
            if self.t2x0['bg'] == 'SystemButtonFace':
                self.t2x0['bg'] = verde_fosco
                self.tabuleiro[2][0] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c2x1(self):
        if not self.minhavez:
            if self.t2x1['bg'] == 'SystemButtonFace':
                self.t2x1['bg'] = verde_fosco
                self.tabuleiro[2][1] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c2x2(self):
        if not self.minhavez:
            if self.t2x2['bg'] == 'SystemButtonFace':
                self.t2x2['bg'] = verde_fosco
                self.tabuleiro[2][2] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def destroy(self):
        self.frame0.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.framel0.destroy()
        self.framel1.destroy()
        self.framel2.destroy()

        # elementos para ajuste da interface.
        self.nada.destroy()
        self.t0x0.destroy()
        self.t0x1.destroy()
        self.t0x2.destroy()
        self.t1x0.destroy()
        self.t1x1.destroy()
        self.t1x2.destroy()
        self.t2x0.destroy()
        self.t2x1.destroy()
        self.t2x2.destroy()
        self.mensagem.destroy()
        self.denovo.destroy()
        self.title.destroy()

    def novo_jogo(self):
        self.destroy()
        self.__init__(self.interface)


tela = tkinter.Tk()
jogo_velha(tela)
tela.mainloop()
