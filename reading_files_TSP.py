"""
Este arquivo lê algumas instâncias de problemas TSP
Autor: Cláudio Lucio
Obs.: Feito para disciplina de PAA do CEFET-MG - 2018/1
"""

def le_tsplib_siXXXX(filename):
    try:
        f = open(filename)
        line = f.readline()
        while line.find("DIMENSION") == -1:
            line = f.readline()
        n = int(line.split()[-1])
        c = {}
        i, j = 1, 1
        while line.find("EDGE_WEIGHT_SECTION") == -1:
            line = f.readline()
        line = f.readline()
        while line.find("EOF"):
            for data in line.split():
                c[i, j] = int(data)
                j += 1
                if j > n:
                    i += 1
                    j = i
                if i == n:
                    return range(1, n + 1), c,
            line = f.readline()
    finally:
        f.close()

def le_tsplib_paXXXX(filename):
            try:
                f = open(filename)
                line = f.readline()
                while line.find("DIMENSION") == -1:
                    line = f.readline()
                n = int(line.split()[-1])
                c = {}
                i, j = 1, 1
                while line.find("EDGE_WEIGHT_SECTION") == -1:
                    line = f.readline()
                line = f.readline()
                while line.find("EOF"):
                    for data in line.split():
                        c[j, i] = int(data)
                        j += 1
                        if j > i:
                            i += 1
                            j = 1
                        if i > n:
                            return range(1, n + 1), c
                    line = f.readline()
            finally:
                f.close()


def imprime_tsplib(V,c):
    print(len(V), "Vertices,", len(c), "Arestas")
    print("Matriz de distâncias:")
    for i in V:
        print('linha: ', i,'-->', end=' ' )
        for j in V:
            if j > i:
                print(c[i, j], end=' ')
            elif j < i:
                print
                print(c[j, i], end=' ')
            else:
                print(0, end=' ')
        print('<-->fim da linha')
    print('<-->fim da matriz')


if __name__ == "__main__":

    path = 'C:\\Users\\claud\\OneDrive\\CEFET\\2018-1 PAA\\trabalho Pratico\\'

    #Arquivo si535
    file_si535 ='si535.tsp'
    V, c  = le_tsplib_siXXXX(path+file_si535)
    imprime_tsplib(V,c)

    # Arquivo si1032
    file_si1032 = 'si1032.tsp'
    V, c = le_tsplib_siXXXX(path + file_si1032)
    imprime_tsplib(V, c)

    # Arquivo pa561
    file_pa561 = 'pa561.tsp'
    V, c = le_tsplib_paXXXX(path + file_pa561)
    imprime_tsplib(V, c)