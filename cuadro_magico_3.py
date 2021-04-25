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

print("original")
for i in range(m):
	print(matriz[i])

for i in range(gen):
	
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

	fit = fitness(rep)
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
	num_max = max(val)
	num_min = min(val)
	index_max = val.index(num_max)
	index_min = val.index(num_min)
	"""
	print("max %d"%(num_max))
	print("min %d"%(num_min))
	print("index max %d"%(index_max))
	print("index min %d"%(index_min))
	"""
	pos_max = index_max % n
	pos_min = index_min % n
	"""
	print("pos max %d"%(pos_max))
	print("pos min %d"%(pos_min))
	"""
	#empieza mutacion
	if((index_max < n) and (index_min < n)): #maximo y minimo en fila
		
		col=random.randint(0,n-1)
		col1=random.randint(0,n-1)

		temp = nuevo[pos_max][col]
		nuevo[pos_max][col] = nuevo[pos_min][col1]
		nuevo[pos_min][col1] = temp

	elif((index_max < 2*n and index_max > n) and (index_min < 2*n and index_min > n)): #maximo y minimo en columna 
		
		fil=random.randint(0,n-1)
		fil1=random.randint(0,n-1)
		"""
		for i in range(n):
			nuevo[i][pos_max]
			nuevo[i][pos_min]
			print("index < 2*n")
			print(nuevo[i][pos_max])
			print(nuevo[i][pos_min])
		"""
		temp = nuevo[fil][pos_max]
		nuevo[fil][pos_max] = nuevo[fil1][pos_min]
		nuevo[fil1][pos_min] = temp

	elif( (index_max < n) and (index_min < 2*n and index_min > n) ): #maximo en fila y minimo en columna

		fil=random.randint(0,n-1)
		col=random.randint(0,n-1)

		temp = nuevo[pos_max][col]
		nuevo[fil][pos_min] = nuevo[pos_max][col]
		nuevo[pos_max][col] = temp

	elif( (index_min < n) and (index_max < 2*n and index_max > n) ): # minimo en fila y maximo en columna
		fil=random.randint(0,n-1)
		col=random.randint(0,n-1)
		
		temp = nuevo[fil][pos_max]
		nuevo[fil][pos_max] = nuevo[pos_min][col]
		nuevo[pos_min][col] = temp
	"""
	elif( (index_max < len(val) and index_max > 2*n) and (index_min < len(val) and index_min > 2*n)): #maximo en diagonal y minimo en diagonal

	elif( (index_max < len(val) and index_max > 2*n) and (index_min < n) ): #maximo en diagonal y minimo en fila

	elif( (index_min < len(val) and index_min > 2*n) and (index_max < n) ): #minimo en diagonal y maximo en fila

	elif( (index_max < len(val) and index_max > 2*n) and (index_min < 2*n and index_min > n) ): #maximo en diagonal y minimo en columna

	elif( (index_min < len(val) and index_min > 2*n) and (index_max < 2*n and index_max > n) ): #minimo en diagonal y maximo en columna
	"""
	#print("nuevo")
	#for i in range(m):
		#print(nuevo[i])
	
	val_1=valores_matriz(nuevo,n)
	#print("valores de columnas")
	#print(val_1)
	
	#valores_col.append(val)

	rep_1=repeticion(val_1)
	#print("frecuencia")
	#print(rep_1)
	
	#re.append(rep)

	fn = fitness(rep_1)
	#print("fitness %f"%(fn))

	if(fn >= fit):
		
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
print("valores de columnas")
print(val)

rep=repeticion(val)
print("frecuencia")
print(rep)


fit = fitness(rep)

print("fitness %f"%(fit))
	

