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

def valorY(y_inf,y_sup,sz,decimal):
	"""
	Rango inferior = y_inf
	Rango sup = y_sup
	tamaño individuos = sz -> 2^n - 1
	decimal = conversion de individuos
	"""
	return y_inf + decimal * ((y_sup-y_inf)/((pow(2,sz))-1))

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


def select (cruza, n): #numero de individuos a cruzar
	return math.ceil((1-cruza)*n)


def cross (cruza,n):
	return math.ceil((cruza*n)/2)

def mutation(m,n):
	return math.ceil(m*n)


print("\t\tALGORITMO GENETICO\n")

x_sup = float(input("Rango superior x = ")) #b
x_inf = float(input("Rango inferior x = ")) #a
y_sup = float(input("Rango superior y = ")) #b
y_inf = float(input("Rango inferior  y = ")) #a
sz = int(input("Tamaño de la poblacion = ")) #n tamaño de la poblacion
cruza = float(input("Porcentaje de cruza = ")) #r
mutacion = float(input("Porcentaje de mutacion = ")) #m
p = int(input("Precision = ")) #p
gen = int(input("Generaciones = "))
tam_x= math.ceil(math.log2(((x_sup-x_inf)*pow(10,p)+1))) #numero de bits de la poblacion
tam_y= math.ceil(math.log2(((y_sup-y_inf)*pow(10,p)+1)))
tam = tam_x+tam_y
print("FORMULAS DE FITNESS\n\t 1)( (1-x)^2 * e^(-x^2-(y+1)^2)) - (x-x^3-y^3)*e^(-x^2-y^2))\n\t 2)21.5 + (x*sin(4*pi*x)) + (y*sin(20*pi*y))\n\t 3)[ 16*x*(1-x)*y*(1-y)*sin(4*pi*x)*sin(4*pi*y) ]^2")
f = int(input("Fitness a utilizar: "))


cast = 0
ind = ""
#veces = 0
fit = 0.0
x = 0.0

individuo = list();
ruleta = list();
fn = list();
fitness_max=list();
x_value = list();
y_value = list();
auxh =list();
h=list();
generacion = list();

promedio = list();

for i in range(sz):

	indx = crearIndividuo(tam_x)
	indy = crearIndividuo(tam_y)
	castx = int(str(indx),2)
	casty = int(str(indy),2)
	ind = indx+indy
	individuo.append(ind)
	
		
	x = valorX(x_inf,x_sup,tam_x,castx) #calculo de x
	x_value.append(x)

	y = valorX(y_inf,y_sup,tam_y,casty) #calculo de x
	y_value.append(y)

	if(f==1):
		fit = fitness_a(x,y)
		if fit > 0:
			fn.append(fit)
		else: 
			fn.append(0)
	if(f==2):
		fit = fitness_b(x,y)
		if fit > 0:
			fn.append(fit)
		else: 
			fn.append(0)
	if(f==3):
		fit = fitness_c(x,y)
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

	for it in range(c*2): # seleccion de individuos aptos para cruza
		r = 0.0
		fi = 0

		r=random.uniform(0.0,maximo)
		for i in range(len(ruleta)):
			if r < ruleta[i]:
				fi = i
				break

		h.append(individuo[fi]) # individuos a cruzar

	bits = math.ceil(tam/2)

		#se generan nuevos individuos y se actualiza la nueva poblacion de acuerdo al coeficiente de cruza
	for i in range(c):
		h1 = ""
		h2 = ""
		tmp = ""
		tmp1 = ""
		tmp2 = ""
		tmp3 = ""
		hn1 = ""
		hn2 = ""
		#print (i)

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
	
	#se actualiza la generacion anterior con la nueva generacion
	for k in range(len(individuo)):
		hip = individuo[i]
		indx = hip[0:tam_x]
		indy = hip[tam_x:tam]
		castx = int(str(indx),2)
		casty = int(str(indy),2)
		
		individuo.append(hip)
		
			
		x = valorX(x_inf,x_sup,tam_x,castx) #calculo de x
		x_value.append(x)

		y = valorX(y_inf,y_sup,tam_y,casty) #calculo de y
		y_value.append(y)


		if(f==1):
			fit = fitness_a(x,y)
			if fit > 0:
				fn.append(fit)
			else: 
				fn.append(0)
		if(f==2):
			fit = fitness_b(x,y)
			if fit > 0:
				fn.append(fit)
			else: 
				fn.append(0)
		if(f==3):
			fit = fitness_c(x,y)
			if fit > 0:
				fn.append(fit)
			else: 
				fn.append(0)



plt.plot(generacion,promedio)

plt.xlim(0,gen+1)
if(f == 1):
	plt.ylim(-3,3)
if(f == 2):
	plt.ylim(-50,50)
if(f == 3):
	plt.ylim(-1,1)

plt.xlabel("Generaciones")
plt.ylabel("Promedio")

plt.show()


