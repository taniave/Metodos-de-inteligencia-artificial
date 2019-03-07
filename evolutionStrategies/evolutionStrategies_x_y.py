import random
import math
import matplotlib.pyplot as plt

escala = 1

def crearIndividuo(x_sup,x_inf):

	nd = random.uniform(x_sup,x_inf)

	return nd

def fitness_a(x,y):
	a = 1-x
	b = y+1
	c = pow(x,2)
	d = pow(y,2)
	e = pow(x,3)
	f = pow(y,3)
	g = pow(a,2)
	h = pow(b,2)
	i = -c-h
	j = x-e-f
	k = -c-d

	return ( g * math.exp(i) ) - (  j * math.exp(k) )

def fitness_b(x,y):
	return 21.5 + (x*math.sin(4*math.pi*x)) + (y*math.sin(20*math.pi*y))

def fitness_c(x,y):
	h = 16*x*(1-x)*y*(1-y)*math.sin(4*math.pi*x)*math.sin(4*math.pi*y)
	
	return pow(h,2)
	
def normal_x():
	z1 = random.uniform(0.0,1.0)
	z2 = random.uniform(0.0,1.0)

	c = math.cos(2*math.pi*z2)
	f = math.sqrt(-2*math.log(z1))

	return c*f

def normal_y():
	z1 = random.uniform(0.0,1.0)
	z2 = random.uniform(0.0,1.0)

	c = math.sin(2*math.pi*z2)
	f = math.sqrt(-2*math.log(z1))

	return c*f


def cross(cruza,num_ind):
	return cruza*num_ind

def mutacion(mu,num_ind):
	return mu*num_ind

def burbuja(fn,individuo_x,individuo_y): #metodo de oredenamieto utilizado para ordenar las listas de fitness e indivudos tomando como referencia el fitness
	for j in range(len(fn)-1,0,-1):
		for i in range(j):
			if fn[i]<fn[i+1]:

				temp = fn[i]
				fn[i] = fn[i+1]
				fn[i+1] = temp

				temp2 = individuo_x[i]
				individuo_x[i] = individuo_x[i+1]
				individuo_x[i+1] = temp2

				temp3 = individuo_y[i]
				individuo_y[i] = individuo_y[i+1]
				individuo_y[i+1] = temp3

def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

print("\t\tALGORITMO ESTRATEGIAS EVOLUTIVAS DOS VARIABLES\n")


print("FORMULAS DE FITNESS\n\t 1)( (1-x)^2 * e^(-x^2-(y+1)^2)) - (x-x^3-y^3)*e^(-x^2-y^2))\n\t 2)21.5 + (x*sin(4*pi*x)) + (y*sin(20*pi*y))\n\t 3)[ 16*x*(1-x)*y*(1-y)*sin(4*pi*x)*sin(4*pi*y) ]^2")
formula = int(input("Fitness a utilizar = "))
x_sup = float(input("Rango superior x = ")) #b
x_inf = float(input("Rango inferior x = ")) #a
y_sup = float(input("Rango superior y = ")) #b
y_inf = float(input("Rango inferior y = ")) #a
sz = int(input("Tamaño de la poblacion = ")) #mu
num_ind = int(input("Numero de individuos nuevos por iteracion = ")) #lambda
cruza = float(input("Porcentaje de cruza = ")) #r
mu = float(input("Porcentaje de mutacion = ")) #m


individuo_x = list();
individuo_y = list();
fn = list();
promedio = list();
generacion = list();
h_y = list();
hi_y = list();

# se crea la generacion incial y se calculan fitness, valor de x para cada individuo
for i in range(sz):
	ind_x = crearIndividuo(x_sup,x_inf)
	ind_y = crearIndividuo(y_sup,y_inf)
	individuo_x.append(ind_x)
	individuo_y.append(ind_y)
	

	if(formula == 1):
		fit = fitness_a(ind_x,ind_y)
		fn.append(fit)
	if(formula == 2):
		fit = fitness_b(ind_x,ind_y)
		fn.append(fit)
	if(formula == 3):
		fit = fitness_c(ind_x,ind_y)
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

		# EMPIEZA PROCESO DE MUTACION DE LA GENERACION
		m = math.ceil(mutacion(mu,num_ind)) #mutacion

		h_x = random.sample(individuo_x,m)
		
		for i in range(len(h_x)):
			aux = 0.0
			index = 0
			tmp = 0.0

			aux = h_x[i]
			index = search(individuo_x,aux)
			tmp = individuo_y[index]
			#print("index = %d individuo x= %f individuo_y = %f"%(index,aux,tmp))
			h_y.append(tmp)
		
		for i in range(m):
			hip_x = 0.0
			hip_y = 0.0

			hip_x = h_x.pop()
			hip_y = h_y.pop()

			n = normal_x()*escala
			norm = normal_y()*escala

			tmp_x = hip_x+n
			if(tmp_x > x_sup):
				tmp_x = x_sup
			elif(tmp_x < x_inf):
				tmp_x = x_inf

			individuo_x.append(tmp_x)

			tmp_y = hip_y+norm
			if(tmp_y > y_sup):
				tmp_y = y_sup
			elif(tmp_y < y_inf):
				tmp_y = y_inf
			
			individuo_y.append(tmp_y)
			
			if(formula == 1):
				f = fitness_a(tmp_x,tmp_y)
				fn.append(f)
			if(formula == 2):
				f = fitness_b(tmp_x,tmp_y)
				fn.append(f)
			if(formula == 3):
				f = fitness_c(tmp_x,tmp_y)
				fn.append(f)

			


		#INICIA CRUZA DE INDIVIDUOS
		#seleccion de individuos candidatos a cruza
		cant = math.ceil(cross(cruza,num_ind))


		hi_x = random.sample(individuo_x,cant)# se seleccionan de manera aleatoria con probabilidad uniforme de cruza
		
		for i in range(len(hi_x)):
			aux = 0.0
			index = 0
			tmp = 0.0

			aux = hi_x[i]
			index = search(individuo_x,aux)
			tmp = individuo_y[index]
			#print("index = %d individuo x= %f individuo_y = %f"%(index,aux,tmp))
			hi_y.append(tmp)
		
		for i in range(cant-1):# cruza

			h1_x=0.0
			h2_x=0.0
			tmp_x = 0.0
			h1_y=0.0
			h2_y=0.0
			tmp_y = 0.0

			h1_x = hi_x.pop()
			h2_x = hi_x.pop()
			tmp_x = (h1_x+h2_x)/2 # se realiza la cruza de individuos calculando el promedio del par seleccionado
			individuo_x.append(tmp_x)

			h1_y = hi_y.pop()
			h2_y = hi_y.pop()
			tmp_y = (h1_y+h2_y)/2 # se realiza la cruza de individuos calculando el promedio del par seleccionado
			individuo_y.append(tmp_y)

			if(formula == 1):
				f = fitness_a(tmp_x,tmp_y)
				fn.append(f)
			if(formula == 2):
				f = fitness_b(tmp_x,tmp_y)
				fn.append(f)
			if(formula == 3):
				f = fitness_c(tmp_x,tmp_y)
				fn.append(f)
		hi_x.clear()
		hi_y.clear()
		h_x.clear()		
		h_y.clear()

		burbuja(fn,individuo_x,individuo_y) # se ordenan las listas de fitness e individuos de mayor a menor 
		
		#se descartan aquellos individuos que se encuentren por debajo del tamaño de la poblacion establecido
		del individuo_x[sz:]
		del individuo_y[sz:]
		del fn[sz:]

		fn_mx=max(fn) # se guarda el valor maximo de fitness de la poblacion

		if(fness < fn_mx):
			fness = fn_mx
			di = individuo_x[0]
			di_y = individuo_y[0]
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

print("  ------------------------------------------------------------------------------------------")
print(" | Generacion = %d | Mejor individuo = %f , %f | Fitness maximo = %f | " %(x,di,di_y,fness))
print("  ------------------------------------------------------------------------------------------")	

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