
# -*- coding: utf-8 -*-
"""
Este arquivo resolve instâncias de problemas TSP usando algumas heuristicas: DFS
Autor: Cláudio Lucio
Obs.: Feito para disciplina de PAA do CEFET-MG - 2018/1
"""

import random
import sys
#sys.path('C:\\Users\\claud\\PycharmProjects\\Algorithm-Jokes-in-Python\\')
import reading_files_TSP as rst
import solving_TSP_FB as FB
from random import shuffle


def DFS_Visit(v,cor,pi,c,tempo,f,d):
    cor[v-1]='C'   #Branco, o vertice v acaba ser visitado
    tempo[0] += 1
    #print('tempo d: ', tempo[0])
    d[v-1]=tempo[0]
    for adj_v in range(v,len(cor)+1):
        if cor[adj_v-1] == 'B':
            pi[adj_v-1] = v
            DFS_Visit(adj_v,cor,pi,c,tempo,f,d)
    cor[v - 1] = 'P'
    tempo[0] += 1
    #print('tempo f: ',tempo[0])
    f[v -1] = tempo[0]


def DFS_Visit_menor_vizinho(v, cor, pi, c, tempo, f, d,ordem_visita):
    cor[v - 1] = 'C'  # Branco, o vertice v acaba ser visitado
    tempo[0] += 1
    ordem_visita.append(v)
    #print('tempo d: ', tempo[0])
    d[v - 1] = tempo[0]
    for adj_v in range(1, len(cor)):
        path_menor = 10000000000
        v_menor = adj_v
        for menor in range(1, len(cor)):
            if v > menor:
                dist = c[menor,v]
            else:
                dist = c[v,menor]
            if (cor[menor-1] == 'B') and (dist < path_menor) and (dist != 0):
                v_menor = menor
                #print('---',menor,'Era: ',path_menor, ' foi para:' ,dist)
                path_menor = dist
        if cor[v_menor-1] == 'B':
            pi[v_menor-1] = v_menor
            DFS_Visit_menor_vizinho(v_menor, cor, pi, c, tempo, f, d,ordem_visita)
        # c[v,adj_v+1]
    cor[v - 1] = 'P'
    tempo[0] += 1
    #print('tempo f: ', tempo[0])
    f[v - 1] = tempo[0]




def DFS(V,c):
    global cor  #coloração do vertice
    global pi   # antecessor
    global d   #tempo de descoberta do vertice
    global f    #tempo em que todos os adjacentes já foram explorados
    cor = []
    pi = []
    d = []
    f = []
    global tempo
    tempo = []
    tempo.append(0)
    for i,v in  enumerate(V):
        cor.append('B')   #insere com branco
        pi.append(0)      # sem antecessor
        d.append(0)       #tempo da descoberto
        f.append(0)       # tempo final da inicialização
    for i, v in enumerate(V):
        if cor[i-1] == 'B':
            #print(cor[i-1],v)
            DFS_Visit(v,cor,pi,c,tempo,f,d)
    return [x+1 for x in pi]


def DFS_menor_vizinho(V,c):
    global cor  #coloração do vertice
    global pi   # antecessor
    global d   #tempo de descoberta do vertice
    global f    #tempo em que todos os adjacentes já foram explorados
    global ordem_visita
    cor = []
    pi = []
    f = []
    f = []
    ordem_visita = []
    global tempo
    tempo = []
    tempo.append(0)

    for i,v in  enumerate(V):
        cor.append('B')   #insere com branco
        pi.append(0)      # sem antecessor
        d.append(0)       #tempo da descoberto
        f.append(0)       # tempo final da inicialização
    for i, v in enumerate(V):
        if cor[i-1] == 'B':
            #print(cor[i-1],v)
            DFS_Visit_menor_vizinho(v,cor,pi,c,tempo,f,d,ordem_visita)
    return [x for x in ordem_visita]


#Faz o calculo da distância de cada rota
def calc_distancia_rota (todas_rotas,c):
    distancia_rota=[]
    for i in range(0,len(todas_rotas)):
        distancia_rota.append(0)
        for j,item_rota in enumerate(todas_rotas[i]):
            if j != len(todas_rotas[i])-1:
                if item_rota < todas_rotas[i][j + 1]:
                    distancia_rota[i] +=  c[item_rota, todas_rotas[i][j + 1]]
                else:
                    distancia_rota[i] += c[todas_rotas[i][j + 1],item_rota]
            else:
                distancia_rota[i] += c[1, todas_rotas[i][j]]
    return distancia_rota

if __name__ == "__main__":

    path = 'C:\\Users\\claud\\OneDrive\\CEFET\\2018-1 PAA\\trabalho Pratico\\'

    #Arquivo si535
    file_si535 ='si535.tsp'
    V, c  = rst.le_tsplib_siXXXX(path+file_si535)
    #rst.imprime_tsplib(V,c)
    rota = [DFS(V, c)]
    distancias_rota = calc_distancia_rota(rota, c)
    print('Distância usando DFS:',str(distancias_rota).replace('[','').replace(']',''))
    rota_menor_vizinho = [DFS_menor_vizinho(V, c)]
    distancias_rota_menor_vizinho = calc_distancia_rota(rota_menor_vizinho, c)
    print('Distância usando DFS menor vizinho:', str(distancias_rota_menor_vizinho).replace('[', '').replace(']', ''))


    # Arquivo si1032
    file_si1032 = 'si1032.tsp'
    V, c = rst.le_tsplib_siXXXX(path + file_si1032)
    #rst.imprime_tsplib(V, c)
    rota = [DFS(V, c)]
    distancias_rota = calc_distancia_rota(rota, c)
    print('Distância usando DFS:', str(distancias_rota).replace('[', '').replace(']', ''))
    rota_menor_vizinho = [DFS_menor_vizinho(V, c)]
    distancias_rota_menor_vizinho = calc_distancia_rota(rota_menor_vizinho, c)
    print('Distância usando DFS menor vizinho:', str(distancias_rota_menor_vizinho).replace('[', '').replace(']', ''))

    # Arquivo pa561
    file_pa561 = 'pa561.tsp'
    V, c = rst.le_tsplib_paXXXX(path + file_pa561)
    #rst.imprime_tsplib(V, c)
    rota = [DFS(V, c)]
    distancias_rota = calc_distancia_rota(rota, c)
    shuffle(rota)
    distancias_rota = calc_distancia_rota(rota, c)
    print('Distância usando DFS:', str(distancias_rota).replace('[', '').replace(']', ''))
    rota_menor_vizinho = [DFS_menor_vizinho(V, c)]
    distancias_rota_menor_vizinho = calc_distancia_rota(rota_menor_vizinho, c)
    print('Distância usando DFS menor vizinho:', str(distancias_rota_menor_vizinho).replace('[', '').replace(']', ''))