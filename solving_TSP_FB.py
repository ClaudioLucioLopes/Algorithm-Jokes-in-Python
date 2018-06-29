# -*- coding: utf-8 -*-
"""
Este arquivo gera instâncias de problemas TSP e às resolve por força bruta
Autor: Cláudio Lucio
Obs.: Feito para disciplina de PAA do CEFET-MG - 2018/1
"""

import random
import sys
#sys.path('C:\\Users\\claud\\PycharmProjects\\Algorithm-Jokes-in-Python\\')
import reading_files_TSP as rst

#Faz o calculo da distância de cada rota
def calc_distancia_rota (todas_rotas,c):
    distancia_rota=[]
    for i in range(0,len(todas_rotas)):
        distancia_rota.append(0)
        for j,item_rota in enumerate(todas_rotas[i]):
            if j != len(todas_rotas[i])-1:
                distancia_rota[i] +=  c[item_rota, todas_rotas[i][j + 1]]
            else:
                distancia_rota[i] +=  c[todas_rotas[i][j ], todas_rotas[i][0]]
    return distancia_rota

#gera uma matriz(na verdade um dicionário no python) de pesos aleatórios
def gera_matriz_pesos(V_num):
    V = range(1, V_num + 1)
    # Geração da matriz de pesos aleatórias entre 1 e 20
    min_pes = 1
    max_pes = 20
    random.seed(12345)
    c = {}
    for i in V:
        print(i)
        j = i + 1
        c[i, i] = 0
        while j <= TS_instance:
            c[i, j] = random.randint(min_pes, max_pes)
            c[j, i] = c[i, j]
            j += 1
    return c

if __name__ == "__main__":
    import time
    import itertools
    N_TSP_problems = 13  #Tamanho máximo dos problemas que serão resolvidos via força bruta
    TSP_problems = [i for i in  range(2,N_TSP_problems+1)]



    time_history = []
    for TS_instance in TSP_problems:
        #Obtem o tamanho da instância que será tratada
        #TS_instance = TSP_problems[3]

        start_time = time.time()
        #Vertices do problema
        V = range(1,TS_instance+1)
        #Gera a matriz de valores aleatorios
        c = gera_matriz_pesos(TS_instance)

        #rst.imprime_tsplib(V,c)

        l_V = [item for item in V][1:] # cria a lista de rotas sem a cidade origem
        #gera todas as rotas usando permutação dos vertices
        todas_rotas = list(map(list, itertools.permutations(l_V)))
        #adiciona a mesma cidade origem
        for item in todas_rotas:
            item.insert(0, 1)

        todas_distancias_rota = calc_distancia_rota(todas_rotas,c)
        #Imprime a primeira menor rota - pois pode haver empate
        print('Número de vértices:',TS_instance)
        print('Rota:',todas_rotas[todas_distancias_rota.index(min(todas_distancias_rota))])
        print('Distância:',todas_distancias_rota[todas_distancias_rota.index(min(todas_distancias_rota))])
        aux = (time.time() - start_time)
        time_history.append(aux)
        print("--- %s Segundos ---" % aux)

    import seaborn as sns
    sns.set_style("whitegrid")
    sns.tsplot(time_history, TSP_problems)