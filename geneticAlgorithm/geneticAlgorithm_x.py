import random
import math
import copy
import matplotlib.pyplot as plt


def crearIndividuo(tam):
	nd = ""
	for i in range(tam):
		nd+=str(random.randint(0,1))
	return nd

def valorX(x_inf,x_sup,sz,decimal):
	"""
	Rango inferior = x_inf
	Rango sup = x_sup
	tamaño individuos = sz -> 2^n - 1
	decimal = conversion de individuos
	"""
	return x_inf + decimal * ((x_sup-x_inf)/((pow(2,sz))-1))

def fitness(x):
	return x*math.sin(10*math.pi*x)+1.0

def select (cruza, n): #numero de individuos a cruzar
	return math.ceil((1-cruza)*n)


def cross (cruza,n):
	return math.ceil((cruza*n)/2)

def mutation(m,n):
	return math.ceil(m*n)


print("\t\tALGORITMO GENETICO\n")

x_sup = int(input("Rango superior = ")) #b
x_inf = int(input("Rango inferior = ")) #a
sz = int(input("Tamaño de la poblacion = ")) #n tamaño de la poblacion
cruza = float(input("Porcentaje de cruza = ")) #r
mutacion = float(input("Porcentaje de mutacion = ")) #m
p = int(input("Precision = ")) #p
gen = int(input("Generaciones = "))
tam = math.ceil(math.log2(((x_sup-x_inf)*pow(10,p)+1))) #numero de bits de la poblacion



cast = 0
ind = ""

fit = 0.0
x = 0.0

individuo = list();
ruleta = list();
fn = list();
fitness_max=list();
x_value = list();
auxh=list();
h=list();
generacion = list();

promedio = list();

# se crea la generacion incial y se calculan fitness, valor de x para cada individuo
for i in range(sz):
	ind = crearIndividuo(tam)
	individuo.append(ind)
	cast = int(str(ind),2)
		
	x = valorX(x_inf,x_sup,tam,cast) #calculo de x
	x_value.append(x)

	fit = fitness(x)
	if fit > 0:
		fn.append(fit)
	else: 
		fn.append(0)

for x in range(gen):
	generacion.append(x);
	
	rul=0.0

	for i in range(len(fn)):
		rul+=fn[i]
		ruleta.append(rul)
	
	maximo = max(ruleta)
	ma = max(fn)
	prom = maximo/sz
	promedio.append(prom)
	cant = select(cruza,sz)
	c = cross(cruza,sz)
	size=len(fitness_max)

	if(gen % 10 == 0): # se aumenta el valor de mutacion al doble si la poblacion va empeorando en dado nuemro de iteraciones
		for j in range(size):
			if ma == fitness_max[j]:
				mutacion*=2

	


	for it in range(cant):
		r = random.uniform(0.0,maximo)
		#print("%f"%(r))	
		for i in range(len(ruleta)):
			if r < ruleta[i]:
				fi = i
				break
		
		auxh.append(individuo[fi]) # inicio de nueva generacion 	

	for it in range(c*2):
		r = 0.0
		fi = 0

		r=random.uniform(0.0,maximo)
		for i in range(len(ruleta)):
			if r < ruleta[i]:
				fi = i
				#print("pos en fitness %d"%(fi))
				#print(fn[fi])
				break
		h.append(individuo[fi]) # individuos a cruzar

	bits = math.ceil(tam/2)

		#se generan nuevos individuos y se actualiza la nueva poblacion de acuerdo al porcentaje de cruza 
	for i in range(c):
		h1 = ""
		h2 = ""
		tmp = ""
		tmp1 = ""
		tmp2 = ""
		tmp3 = ""
		hn1 = ""
		hn2 = ""
		
		h1 = h.pop()
		h2 = h.pop()
		tmp = h1[0:bits]
		tmp1 = h1[bits:tam]
		tmp2 = h2[0:bits]
		tmp3 = h2[bits:tam]
		hn1=tmp+tmp3
		hn2=tmp2+tmp1
		auxh.append(hn1)
		auxh.append(hn2)
	
	
	mu = mutation(mutacion,sz)

	#se hace la mutacion de los individuos de la poblacion nueva que se seleccionaron al azar
	for i in range(mu):
		t1=""
		t2=""
		t3=""
		a = ""
		au = ""
		u=""
		ra = 0
		a = random.choice(auxh)
		ra = random.randint(1,tam-1)
		au=a
		
		
		t1=au[0:ra-1]
		t2 = au[ra-1:ra]
		t3 = au[ra:tam]
		
		if t2 == '0':
			t2=t2.replace('0','1')
			
		else:
			t2=t2.replace('1','0')
			
		u = t1+t2+t3
		
	for j in range(len(auxh)):

		if a in auxh[j]:
			auxh[j] = u
			break 

	individuo.clear()
	individuo = auxh.copy()

	ruleta.clear()
	fn.clear()
	x_value.clear()
	auxh.clear()
	h.clear()
	
	for k in range(len(individuo)):
		hip = individuo[k]
		cast = int(str(hip),2)
		
		x = valorX(x_inf,x_sup,tam,cast) #calculo de x
		x_value.append(x)

		fit = fitness(x)
		if fit > 0:
			fn.append(fit)
		else: 
			fn.append(0)

plt.plot(generacion,promedio)

plt.xlim(0,gen+1)
plt.ylim(0,3)
plt.xlabel("Generaciones")
plt.ylabel("Promedio")

plt.show()