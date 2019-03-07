import random
import math
import matplotlib.pyplot as plt

escala = 1

def crearIndividuo(x_sup,x_inf):

	nd = random.uniform(x_sup,x_inf)

	return nd

def fitness(x):
	return x*math.sin(10*math.pi*x)+1.0
	
def normal():
	z1 = random.uniform(0.0,1.0)
	z2 = random.uniform(0.0,1.0)

	c = math.cos(2*math.pi*z2)
	f = math.sqrt(-2*math.log(z1))

	return c*f

def cross(cruza,num_ind):
	return cruza*num_ind

def mutacion(mu,num_ind):
	return mu*num_ind

def burbuja(fn,individuo): #metodo de oredenamieto utilizado para ordenar las listas de fitness e indivudos tomando como referencia el fitness
	for j in range(len(fn)-1,0,-1):
		for i in range(j):
			if fn[i]<fn[i+1]:
				temp = fn[i]
				temp2 = individuo[i]
				fn[i] = fn[i+1]
				individuo[i] = individuo[i+1]
				fn[i+1] = temp
				individuo[i+1] = temp2


print("\t\tALGORITMO ESTRATEGIAS EVOLUTIVAS\n")

x_sup = float(input("Rango superior = ")) #b
x_inf = float(input("Rango inferior = ")) #a
sz = int(input("Tamaño de la poblacion = ")) #mu
num_ind = int(input("Numero de individuos nuevos por iteracion = ")) #lambda
cruza = float(input("Porcentaje de cruza = ")) #r
mu = float(input("Porcentaje de mutacion = ")) #m
#gen = int(input("generaciones ="))



individuo = list();
fn = list();
promedio = list();
generacion = list();

# se crea la generacion incial y se calculan fitness, valor de x para cada individuo
for i in range(sz):
	ind = crearIndividuo(x_sup,x_inf)
	individuo.append(ind)
	fit = fitness(ind)
	fn.append(fit)

fness = max(fn)

fn_mx = 0.0
cont = -300
x=0
veces = 0

while(veces <  3):
	while(cont < 100):
		x+=1
		generacion.append(x)
		prom = 0.0
		for i in range(len(fn)):
			prom+=fn[i]

		p = prom/sz

		promedio.append(p)


		m = math.ceil(mutacion(mu,num_ind)) #mutacion

		h = random.sample(individuo,m)

		for i in range(m):
			hip = 0.0
			hip = h.pop()
			n = normal()*escala
			tmp = hip+n
			if(tmp > x_sup):
				tmp = x_sup
			elif(tmp < x_inf):
				tmp = x_inf
			individuo.append(tmp)
			f = fitness(tmp)
			fn.append(f)
		

		#INICIA CRUZA DE INDIVIDUOS


		#seleccion de individuos candidatos a cruza
		cant = math.ceil(cross(cruza,num_ind))
		

		hi = random.sample(individuo,cant)# se seleccionan de manera aleatoria con probabilidad uniforme de cruza
		

		for i in range(cant-1):# cruza
				h1=0.0
				h2=0.0
				tmp = 0.0
				h1 = hi.pop()
				h2 = hi.pop()
				tmp = (h1+h2)/2 # se realiza la cruza de individuos calculando el promedio del par seleccionado
				individuo.append(tmp)
				f = fitness(tmp)
				fn.append(f)	
		
		
		hi.clear()
		h.clear()

		burbuja(fn,individuo) # se ordenan las listas de fitness e individuos de mayor a menor 
		
		#se descartan aquellos individuos que se encuentren por debajo del tamaño de la poblacion establecido
		del individuo[sz:]
		del fn[sz:]

		fn_mx=max(fn) # se guarda el valor maximo de fitness de la poblacion

		if(fness < fn_mx):
			fness = fn_mx
			di = individuo[0]
			cont = 0
			if(veces < 2):
				escala = 1
		else:
			cont+=1



	if(veces < 1):
		escala = 2
	elif(veces == 1):
		escala = 0.5

	#escala = 1
	cont = 0
	veces+=1

print("  ----------------------------------------------------------------------------")
print(" | Generacion = %d | Mejor individuo = %f | Fitness maximo = %f | " %(x,di,fness))
print("  ----------------------------------------------------------------------------")	

p_min=min(promedio)
p_max=max(promedio)
g_max = max(generacion)

#FUNCIONES PARA GRAFICAR LOS RESULTADOS

plt.plot(generacion,promedio)

plt.xlim(0,g_max+1)
plt.ylim(p_min,p_max+(p_max*1.5))
plt.xlabel("Generaciones")
plt.ylabel("Promedio")

plt.show()


