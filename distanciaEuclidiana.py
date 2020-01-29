"""Computacao evolutiva - Grupo: Isadora, Natalia e Veronica"""
""" Qual o melhor lugar para construir um condomínio para estudantes? O ponto fixo e a usp. Quanto mais próximo
for da US > qualidade (distancia) e consequentemente > custo (dinheiro para construcao) """
from random import randint
import math
import os

def grafico(individuos_xy, Z1, Z2,melhores_individuos):
    arq = open('grafico.dot','w')
    arq.write('graph{\n') #cabecalho do arq
    arq.write('\tlabel=\"Legenda\";\n')
    arq.write('\tbgcolor=gray;\n')
    arq.write('\tnodesep=1.0;\n')
    arq.write('\tZ [shape=circle,width=0.7,style=filled,fillcolor=blue, pos=\"' + str(Z1) + ',' + str(Z2) + '!\"];\n')
    cont=0
    #Escreve as caracteristicas do ponto no graphvz
    for x in individuos_xy:
        if x == melhores_individuos[0]:
            arq.write('\tP' + str(cont) +' [shape=square,width=0.7,style=filled,fillcolor=green, pos=\"' + str(x[0]) + ',' + str(x[1]) + '!\"];\n')
        else:
            arq.write('\tP' + str(cont) +' [shape=square,width=0.7,style=filled,fillcolor=red, pos=\"' + str(x[0]) + ',' + str(x[1]) + '!\"];\n')
        cont+=1
    cont=0
    #Define as conexoes do grafo no graphvz
    for x in individuos_xy:
        if x == melhores_individuos[0]:
            arq.write('\tZ--P' + str(cont) +' [label=\"'+str(round(individuos_xy[x],2))+'\",color=green];\n')
        else:
            arq.write('\tZ--P' + str(cont) +' [label=\"'+str(round(individuos_xy[x],2))+'\",color=red];\n')
        cont+=1
    arq.write('\n}')
    arq.close()
    os.system("dot -Kfdp -n -Tpng grafico.dot -o grafico.png")
    
n_min_coord = 1
n_min = 0 #numero minimo de pontos x1
n_max = 20
valor_min = 1 #mil reais
valor_max = 20 #vinte mil reais

"""1 - gerar quantidade de coordenadas em X e Y"""

qntd_pontos = (randint(n_min_coord,n_max)) #qntd de pontos a serem gerados
individuos_xy = {}
individuos_atributos = {}
melhores_individuos = []

"""2 - distancia euclidiana (qualidade)"""

Z1 = (randint(n_min,n_max)) #ponto 1 da distancia
Z2 = (randint(n_min,n_max)) #ponto 2 da distancia


for ponto in range(qntd_pontos):
    pontosx = randint(n_min,n_max)
    pontosy = randint(n_min,n_max) #sorteando o ponto x1 e y1
    
    while (pontosx,pontosy) in individuos_xy: #se ja tiver os pontos vai sortear novamente
        pontosx = randint(n_min,n_max)
        pontosy = randint(n_min,n_max) #sorteando o ponto x1 e y1  

    """3 - Calcula a distancia euclidiana - calcula a qualidade """

    dist = ((Z1-pontosx)**2)+((Z2-pontosy)**2)
    distancia = math.sqrt(dist)
    
    """4 - Preco (custo)"""
    preco = (randint(valor_min,valor_max)) #valor que vai custar

    """5 - APTIDAO (realizado com base em pesos, dando prioridade pela qualidade (distancia))"""

    aptidao = (distancia*0.7)+(preco*0.3)
    #individuos[(x,y)] = [custo,qualidade,outro,outro,...]
    individuos_atributos[(pontosx,pontosy)] = [preco,distancia]
    individuos_xy[(pontosx,pontosy)] = aptidao
    
"""6 - Ordenando as aptidoes"""

for individuo in sorted(individuos_xy, key = individuos_xy.get): 
    print("Individuo: " + str(individuo) + "\tCusto (R$): " + str(individuos_atributos[individuo][0]) + "\tDist(qualidade): " + str(round(individuos_atributos[individuo][1],2)) + "\tAptidao: " + str(round(individuos_xy[individuo],4)))
    melhores_individuos.append(individuo)
    
grafico(individuos_xy,Z1,Z2,melhores_individuos)
         






