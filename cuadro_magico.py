import random
import math

def orden_cuadro(n):
  return (n*(math.pow(n,2)+1))/2

"""
def fitness(ind,num,n):
	suma = 0
	cont = 0
	#for j in range(n):
	for i in range(num-1):
		cont+=1
		suma += ind[i]
		if(cont == n):
			cont = 0
			print("suma fila %d"%(suma))
			suma = 0

	suma = 0
	for i in range(num-1):

		if(i % n == 0):
			suma += ind[i]

	print("suma col 1 %d "%(suma))

	
	suma = 0
	for i in range(num-1):

		if(i % n == 0):
			cont = ind[i]+1
			suma += cont
	print("suma col 2 %d "%(suma))

	suma = 0
	for i in range(num-1):

		if(i % n == 0):
			cont = ind[i]+2
			suma += cont
	print("suma col 3 %d "%(suma))

	p = int((num-2)/2)
	
	suma = ind[0] + ind[p] + ind[num-2]
	
	print("suma diagonal 1 %d "%(suma))
	
	suma = ind[n-1] +ind[p] + ind[num-n-1]
	
	print("suma diagonal 2 %d "%(suma))
"""


def fitness(matriz,n):
	aux = 0
	for i in range(0,n):
		aux+=matriz[i][i]

	for i in range(0,n):
		fil = 0
		for j in range(0,n):
			fil += matriz[i][j]

		if(fil != aux): 
			return False

	for i in range(0,n):
		col = 0
		for j in range(0,n):
			col+=mat[j][i]
		if(aux != col):
			return False
	return True



def ind(m,n):
    result = []
    for i in range(m):
        result.append(list(range(n*i, n*i+n)))

    return result

	
print("SOLUCIONADOR DE CUADROS MAGICOS\n")
n = int(input("Orden del cuadro magico = ")) #tamaño del cuadro magico
#mu = float(input("Mutacion = ")) #porcentaje de mutacion de cada individuo

orden = math.ceil(orden_cuadro(n));

print("Orden = %d"%(orden))
num = (n*n)+1

m = n
matriz = ind(m,n)

for i in range(m):
	for j in range(n):
		matriz[i][j]+=1

print(matriz)

if(fitness(matriz,n)):
	print("es")
else:
	print("no es")

