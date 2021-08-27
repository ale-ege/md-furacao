# import pandas as pd
import numpy as np
import pandas as pd

from prettytable import PrettyTable
from collections import defaultdict

from Furo import Furo

# Variáveis iniciais
nro_cabecotes = 16
nro_brocas = 21
distancia_pinos = 32		# mm
# ----------

# Arquivo
filename = 'DIVISÓRIA 12X387X1652.bpp'
file = open(filename, 'r', encoding='latin1')
# ----------

# Definições
# Side 0 : 0 - Horizontal inferior
# Side 0 : 1 - Vertical esquerda
# Side 0 : 2 - 
# Side 0 : 3 - Vertical direita
# Side 0 : 4 - 
# Side 0 : 5 - Frontal

cabecotes = [i + 1 for i in range(nro_cabecotes)]

for cabecote in cabecotes:
	# vetor = np.array([0 for i in range(nro_pinos)])
	vetor = np.array([0, 1, 2, 3])
    # print(vetor)
	# cabecotes[cabecote] = vetor

# furos = {}
# furos = np.array([])
furos = []
# ----------

count = 0
flag_program = False

for line in file:
	if line.find("PAN=LPX") == 0:
		lpx = line.split('|')[1]
	if line.find("PAN=LPY") == 0:
		lpy = line.split('|')[1]
	if line.find("PAN=LPZ") == 0:
		lpz = line.split('|')[1]

	if line.find("[PROGRAM]") == 0:
		flag_program = True
	elif flag_program:
		nome = line.rstrip('\n')
		flag_program = False

	if line.find("@ BG") == 0:
		# line[ 0]: '@ BG'
		# line[ 1]: '""'
		# line[ 2]: '""'
		# line[ 3]: '37127068'
		# line[ 4]: '""'
		# line[ 5]: side
		# line[ 6]: crn
		# line[ 7]: x
		# line[ 8]: y
		# line[ 9]: z
		# line[10]: dp
		# line[11]: diametro
		# line[12]: p
		# line[13]: cabeçote

		line = line.split(',')
		# print(line)

		# Dados
		side = line[5].removeprefix(' ')
		crn = int(line[6].removeprefix(' ').replace('"', ''))
		x = float(line[7].removeprefix(' '))
		y = float(line[8].removeprefix(' '))
		z = float(line[9].removeprefix(' '))
		dp = float(line[10].removeprefix(' '))
		diametro = float(line[11].removeprefix(' '))
		p = int(line[12].removeprefix(' '))

		broca = str(diametro)
		if (p == 1):
			broca += 'T'

		furo = Furo(
			side,
			crn,
			x,
			y,
			z,
			dp,
			diametro,
			p,
			broca
		)

		# furo = {
		# 	'side': side,
		# 	'crn': crn,
		# 	'x': x,
		# 	'y': y,
		# 	'z': z,
		# 	'dp': dp,
		# 	'diametro': diametro,
		# 	'p': p,
		# 	'broca': broca
		# }

		# furos[count] = furo
		# furos.append(furo)
		furos.append(furo)
		# count = count + 1
		# print(line)
		# print(furo)

# Peca
peca = PrettyTable()
peca.title = nome
peca.field_names = ['Dimensão', 'Valor (mm)']
peca.align = 'l'
peca.add_row(['Comprimento (X)', lpx])
peca.add_row(['Largura (Y)', lpy])
peca.add_row(['Espessura (Z)', lpz])
print(peca)
# ----------

# Tabela de dados
data = PrettyTable()
data.title = filename
data.field_names = ["Side", "CRN", "X", "Y", "Z", "DP", "Diametro", "P", "Broca"]

for i in furos:
	# data.add_row(list(furos[i].values))
	data.add_row(list(i.__dict__.values()))

print(data)
# ----------

# Tabela de cabeçotes
table = PrettyTable()
table.title = 'Cabeçotes'
table.field_names = cabecotes
# data.add_row()
print(table)
# ----------


# Ordenar por side
furos.sort(key=lambda furo: furo.side)

# Agrupar por side
groups = defaultdict(list)
for obj in furos:
    groups[obj.side].append(obj)
furos = list(groups.values())

# Ordenar por X

for array in furos:
    groups = defaultdict(list)
    for obj in array:
        groups[obj.x].append(obj)
    array = list(groups.values())
    print (array)
    
furos = list(groups.values())


# Agrupar por X
# groups = defaultdict(list)
# for obj in furos:
#     groups[obj.side].append(obj)
# new_list = list(groups.values())


# print(new_list[1][0].side)
data = PrettyTable()
data.title = filename
data.field_names = ["Side", "CRN", "X", "Y", "Z", "DP", "Diametro", "P", "Broca"]

for i in furos:
	# data.add_row(list(furos[i].values))
	data.add_row(list(i.__dict__.values()))

print(data)
# furos.map(key=lambda furo: furo.x)



# Caso Side == 0:1 ou Side == 0:3
	# Agrupar elementos onde Y e Side sejam iguais
# Senão
	# Agrupar elementos onde X e Side sejam iguais

# Primeiro cabeçote = 0:1
# Ultimo cabeçote = 0:3






from operator import itemgetter
from itertools import groupby

lki = [["A",0], ["B",1], ["C",0], ["D",2], ["E",2]]
lki.sort(key=itemgetter(1))

# print(lki)
# print(furos)
glo = [[x for x,y in g]
       for k,g in  groupby(lki,key=itemgetter(1))]

# print(glo)