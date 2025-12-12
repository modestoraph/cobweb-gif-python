# -*- coding: utf-8 -*-
import numpy as np
class Funcao(object):

    #Construtor
    def __init__(self, r, s=0.0):
        self.r = r
        self.s = s

    # 1 - Função Logística
    def logistica(self, x):
        return self.r * x * (1 - x)

    # 2 - Função da Reta
    def reta(self, x):
        return self.r * x + self.s

    # 3 - Função Raiz Quadrada
    def raiz(self, x):
        return self.r * np.sqrt(x)

    # 4 - Função Cosseno
    def cosseno(self, x):
        return self.r * np.cos(x)

    # 5 - Função Expansora
    def expansora(self, x):
        return self.r * x % 1

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def val_iterados(f, x0, itera_max):


#        ------------Criação das variáveis de armazenamento------------       #


    iteracao = np.empty(itera_max)  #cria um array vazio para ITERACAO

    fx = np.empty(itera_max)    #Cria uma array vazio para FX

    iteracao[0], fx[0] = 0, x0  #inicia ITERACAO com 0 e FX com o valor x0





#        ------------Armazena os valores dos iterados-------------          #





    for n in range(1,itera_max):  #Itera até o valor máximo de iterações

        iteracao[n] = n     #Guarda cada indice das iterações na lista ITERACAO

        fx[n] = f(fx[n-1])  #Calcula e guarda o valor de todos os iterados, aplicado a f nos valores de x





#     ------------Criação do gráfico dos valores dos iterados------------     #





    plt.figure(figsize=(8, 5))  #Tamanho da figura
    plt.plot(iteracao, fx, color='blue', linestyle='solid', marker='o',
             markerfacecolor='red', markersize=3)   #Detalhes do plot

    plt.xlabel('Iterações') #Título do eixo x

    plt.ylabel('Valor de cada iterado') #Título do eixo y

    plt.title(f'Gráfico dos valores das Iterações') #Titulo do gráfico

    plt.grid(True, alpha=0.5)   #Grade do gráfico

    plt.show()  #Plot do gráfico





#                       -----------COBWEB------------                         #





def cobweb(f, x0, itera_max, limite_x=(0, 1), filename='cobweb.gif'):

    iterado = [x0] #Lista com os iterados do primeiro ponto




#           ------------ Calcular o valor dos iterados ------------           #




    for i in range(itera_max):

        x_prox = f(iterado[-1]) #Calculando o valor dos iterados dada a f

        iterado.append(x_prox)  #Adiciona o valor dos iterados ao final da lista iterado




#               ------------Plotagem dos iterados------------                 #




    pts_x = [x0]    #Criando a lista para os plot do cobweb no eixo x

    pts_y = [x0]    #Criando a lista para os plots do cobweb no eixo y

    for i in range(len(iterado) - 1):   #Percorre a lista iterado completa

        x_n = iterado[i]    #Define a variável x_n para cada entrada de iterado[i]

        x_n_prox = iterado[i+1] #Define x_n+1 para cada próxima entrada de iterado[i+]

        pts_x.extend([x_n, x_n_prox]) #Criando as coordenadas dos plots do eixo x

        pts_y.extend([x_n_prox, x_n_prox])  #Criando as coordenadas dos plots do eixo y




#   ------------Cria o plano cartesiano e os traços das funções------------   #




    cria_f = np.linspace(limite_x[0], limite_x[1], 100) #Cria as linhas das funções

    fig, ax = plt.subplots(figsize=(6, 6)) #Tamanho da figura

    ax.plot(cria_f, f(cria_f), c='#00AF42', lw=2)   #Plot da f escolhida

    ax.plot(cria_f, cria_f, c='#000000', lw=2)  #Plot da função identidade

    ax.set_aspect('equal', adjustable='box')    #Garantindo o mesmo tamanho do eixo X e Y

    ax.set_xlim(limite_x)   #Limites do eixo x

    ax.set_ylim(limite_x)   #Limites do eixo y

    ax.grid(True, alpha=0.5)    #Grade do plano

    line, = ax.plot([], [], c='#D40002', alpha=0.9, lw=1.5) #Linha para armazenar os traços do cobweb




#          ------------Atualização dos frames do gif------------            #




    def atualiza(frame):
        num_pontos = 1 + frame * 2
        line.set_data(pts_x[:num_pontos], pts_y[:num_pontos])
        ax.set_title(f'Iteração: {frame}')  #Plota a quantidade de iterações
        return line,

    frames = len(iterado) - 1   #Total de frames
    ani = FuncAnimation(fig, atualiza, frames=frames, interval=100, blit=True, repeat=False)    #Criando a animação GIF

    print(f"Gerando o {filename}.") #Mensagem ao rodar o Menu
    ani.save(filename, writer='pillow', fps=120)    #Salvando o arquivo GIF
    plt.close(fig)
    print("Cobweb gerado!")    #Mensagem após gerar o GIF

def menu_cobweb():

    print("Gere um cobweb")

#         ------------Criação do Menu e Tratamento de Erro------------        #

    while True:
        print("Escolha a função:")
        print("1 - Logística")
        print("2 - Reta")
        print("3 - Raiz")
        print("4 - Cosseno")
        print("5 - Expansora")

        try:
            opcao = int(input("Digite a opção: "))
            if opcao in [1, 2, 3, 4, 5]:
                break
            else:
                print("Erro! Escolha uma das opções válidas.")
        except ValueError:
            print("A opção deve ser um número inteiro.")

    while True:
        try:
            r = float(input("Digite o valor de r(Para a função logística valores entre 0 e 1): "))
            break
        except ValueError:
            print("Erro! O valor de r deve ser um número do tipo float.")

    s = 0
    if opcao == 2:
        while True:
            try:
                s = float(input("Digite o valor de s: "))
                break
            except ValueError:
                print("Erro! O valor de s deve ser um número do tipo float.")

    while True:
        try:
            x0 = float(input("Digite o valor inicial x0 entre 0 e 1: "))
            break
        except ValueError:
            print("Erro! O valor de x0 deve ser um número do tipo float.")

    while True:
        try:
            itera_max = int(input("Digite o número de iterações itera_max: "))
            if itera_max >= 1:
                break
            else:
                print("O número de iterações deve ser do tipo inteiro positivo.")
        except ValueError:
            print("Erro! O número de iterações deve ser um número inteiro.")

    F = Funcao(r, s)

    if opcao == 1:
        f = F.logistica
    elif opcao == 2:
        f = F.reta
    elif opcao == 3:
        f = F.raiz
    elif opcao == 4:
      f = F.cosseno
    elif opcao == 5:
       f = F.expansora
    else:
        print("Opção de função inválida.")
        return

    try:
        print("Gráfico dos valores dos iterados")
        val_iterados(f, x0, itera_max)
    except Exception as erro:
        print(f"Erro ao plotar o gráfico: {erro}")

    # Animação do Cobweb (Geração do GIF)
    try:
        cobweb(f, x0, itera_max, limite_x=(0, 1), filename='cobweb.gif')
    except Exception as erro:
        print(f"Erro ao gerar o GIF: {erro}")

menu_cobweb()

