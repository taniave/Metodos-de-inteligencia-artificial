import random
import math
import copy

def orden_cuadro(n):
  return (n*(math.pow(n,2)+1))/2


def valores_matriz(matriz,n):
	valores = []

	for i in range(0,n):
		fil = 0
		for j in range(0,n):
			fil += matriz[i][j]
		
		valores.append(fil)
		

	for i in range(0,n):
		col = 0
		for j in range(0,n):
			col+=matriz[j][i]
		
		valores.append(col)

	aux = 0
	for i in range(0,n):
		aux+=matriz[i][i]
	
	valores.append(aux)	

	diag = 0
	for i in range(0,n):
		for j in range(0,n):
			if(i>0 and i<=n):
				diag+=matriz[i-1][0]
	valores.append(diag)

	return valores
	
def ind(m,n):
    result = []
    for i in range(m):
        result.append(list(range(n*i, n*i+n)))

    return result

def repeticion(valores):
	sz = len(valores)

	frecuencia =[] 

	for i in range(sz):
		tmp = valores[i]
		#print(tmp)
		frecuencia.append(valores.count(tmp))
	return frecuencia

def fitness(valores):

	tam = len(valores)
	prom = 0.0

	for i in range(tam):
		prom+=valores[i]

	p = prom/tam

	return p
	
print("SOLUCIONADOR DE CUADROS MAGICOS\n")

n = int(input("Orden del cuadro magico = ")) #tamaño del cuadro magico
gen = int(input("Generaciones = "))

orden = math.ceil(orden_cuadro(n));

print("constante magica = %d"%(orden))
num = (n*n)+1


m = n

matriz = ind(m,n)

for i in range(m):
	for j in range(n):
		matriz[i][j]+=1
print("matriz")
for i in range(m):
	print(matriz[i])

for i in range(gen):
	fit = 0
	#print("gen #%d"%(i))
	
	
	#poblacion.append(matriz)

	val=valores_matriz(matriz,n)
	#print("valores de columnas")
	#print(val)
	#print("\n")
	#valores_col.append(val)

	rep=repeticion(val)
	#print("frecuencia")
	#print(rep)
	#print("\n")
	#re.append(rep)

	fit = fitness(val)
	#fn.append(fit)
	#print("fitness %f"%(fit))
	#print("\n")
	nuevo = copy.deepcopy(matriz);
	"""
	print("nuevo 1 ")
	for i in range(m):
		print(nuevo[i])
	
	print("control matriz 1 ")
	for i in range(m):
		print(matriz[i])
	
	"""
	#matriz.clear();
	#empieza mutacion
	fil1=random.randint(0,n-1)
	fil2=random.randint(0,n-1)
	col1=random.randint(0,n-1)
	col2=random.randint(0,n-1)

	temp = nuevo[fil1][col1]
	nuevo[fil1][col1] = nuevo[fil2][col2]
	nuevo[fil2][col2] = temp
	
	"""
	print("control matriz 2 ")
	for i in range(m):
		print(matriz[i])
	"""
	val_1=valores_matriz(nuevo,n)
	#print("valores de columnas")
	#print(val_1)
	#print("\n")
	#valores_col.append(val)

	rep_1=repeticion(val_1)
	#print("frecuencia")
	#print(rep_1)
	#print("\n")
	#re.append(rep)

	fn = fitness(val_1)
	#print("fitness %d"%(fn))

	if(fn <= fit):
		#print("\n")
		#print("si fn <= fit")
		matriz.clear();
		matriz = copy.deepcopy(nuevo);
		nuevo.clear();
		rep.clear();
		val.clear();
		rep_1.clear();
		val_1.clear();

	else:
		nuevo.clear();
		rep.clear();
		val.clear();
		rep_1.clear();
		val_1.clear();
print("solucion")
for i in range(m):
	print(matriz[i])
val=valores_matriz(matriz,n)
print("valores ")
print(val)
	

rep=repeticion(val)
print("frecuencia")
print(rep)
	

fit = fitness(val)
	
print("fitness %f"%(fit))

