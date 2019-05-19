import math
import statistics as stats

def sigmoide(f):
	return 1/(1+math.exp(-f))

def sigmoide_derivada_salida(t,O):
    return O * (1 - O) * (t - O)

def sigmoide_derivada_oculta(O,w,delta):
	return O*(1-O)*(w*delta)

lr = 0.1 #float(input("Learning rate = "))
n = 2 #int(input("Network inputs = "))
n_h = 2 #int(input("Hidden Layers = "))
n_o = 1 #int(input("Network outputs = "))

x = [[-1,1,0],[-1,0,0],[-1,0,1],[-1,1,1]]
t = [1,0,1,0]

tol = 0.3

pesos_oculta = list();
pesos_salida = list();

f_oculta = list([0]*n);
O_oculta = list([0]*n);

f_salida = list([0]*n_o);
O_salida = list([0]*len(t));

delta_oculta = list([0]*n);
delta_salida = list([0]*len(t));

error = list();

#se inicializan los pesos de las conexiones entre las capas de entrada y 
#capas ocultas -> capa oculta/salida con capa de salida
pesos_oculta=[[0.8,-0.1],[0.5,0.9],[0.4,1.0]]
pesos_salida=[0.3,-1.2,1.1]


		 
"""
print("pesos capa oculta")
for i in range(len(pesos_oculta)):
	print(pesos_oculta[i])
print("pesos capa salida")
for i in range(len(pesos_salida)):
	print(pesos_salida[i])
print("\n")
"""
aciertos = 0
cont = 0
while(aciertos <= len(t)): #controla las epocas
	aciertos = 0
	#prom = 0.0
#print(len(x))
#se realiza la suma de f -> union entre la capa de entrada y la capa oculta para el primer caso
	for k in range(len(x)):#controla los valores de x
		#suma = 0.0

		for j in range(n):
			suma = 0.0

			for i in range(len(x)-1):

				#print("x [%d][%d] %.2f"%(k,i,x[k][i]))
				#print("w [%d][%d] %f"%(i,j,pesos_oculta[i][j]))
				suma+=x[k][i]*pesos_oculta[i][j] # falta agregar ciclo para que itere a travez de toda la tabla de verdad
			#print(j)
			f_oculta[j] = suma #se agrega el resultado de la sumatoria al arreglo de la funcion de la capa oculta
			O_oculta[j] = sigmoide(suma) #se calcula el valor de la sigmoide para cada O (n)[neurona]

		
			#print("f oculta")
			#print(*f_oculta)
			#print("O oculta")
			#print(*O_oculta)
			#print("\n")
		
		suma = 0.0
		

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		#inicia calculo de la union entre la salida de la capa oculta 
		#y la entrada de la ultima neurona del diagrama
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
		suma=x[0][0]*pesos_salida[0] 
		#print(suma)

		for i in range(len(O_oculta)):
			
			
			#print(suma)
			suma+=pesos_salida[i+1]*O_oculta[i]
		#print(suma)
		#f_salida[k] = suma # se agrega el valor de la sumatoria al arreglo que guarda los valores 
		#de la funcion de la capa de salida
		O_salida[k] = sigmoide(suma) #se calcula el valor de la sigmoide y se agrega al rreglo que corresponde con los valores de salida de la red

		
		#print("f salida")
		#print(*f_salida)
		#print("O salida")
		#print(*O_salida)
		
		
		delta_salida[k] = sigmoide_derivada_salida(t[k],O_salida[k]) #se calcula el valor de delta de salida de la ultima neurona
		
		#print("delta salida")
		#print(delta_salida)
		
		#en base al resultado del calculo del valor de delta de salida con ayuda de la derivada de la sigmoide:
		"""
		Se empieza a calcular hacia atras los valores correspondientes a delta en la capa oculta
		"""
		for i in range(len(O_oculta)):
			delta_oculta[i] = sigmoide_derivada_oculta(O_oculta[i],pesos_salida[i+1],delta_salida[k])
		
		#print("delta oculta")
		#print(*delta_oculta)
		
		
		

		#inicia proceso de backtracking para ajustar los pesos de las conexiones entre neuronas

		for i in range (len(delta_oculta)):
			for j in range(len(x)-1):
				#print("lr = %f w[%d][%d] = %f delta_oculta[%d] =%f x[%d][%d] = %f"%(lr,j,i,pesos_oculta[j][i],i,delta_oculta[i],k,j,x[k][j]))
				tmp = lr*delta_oculta[i]*x[k][j] # falta agregar iteraciones para los otros datos de la tabla de verdad
				pesos_oculta[j][i]+=tmp #se actualizan primero los pesos de la cpaa oculta con ayuda del valor de delta que corresponda a la capa de salida 

		pesos_salida[0]+=(lr*delta_salida[k]*x[k][0])#se realiza el mismo proceso para actualizar los pesos de la capa de salida

		"""
		En lo unico que cambia es que ahora se utilizarn los calculos de la sigmoide O(N) y los valores obtenidos para delta de salida

		"""
		
		for i in range(len(O_oculta)):
			pesos_salida[i+1]+=(lr*delta_salida[k]*O_oculta[i])
		
		"""
		print("actualizacion pesos capa oculta")
		for i in range(len(pesos_oculta)):
			print(pesos_oculta[i])
		
		print("actualizacion pesos capa salida")
		for i in range(len(pesos_salida)):
			print(pesos_salida[i])
		
		"""
		#f_oculta.clear();
		#O_oculta.clear(); 
		#f_salida.clear(); 
		#delta_oculta.clear(); 
		#delta_salida.clear(); 
		#print("\n")

	
	print("-------------------")
	#prom = 0.0
	
	for i in range(len(O_salida)):
		error.append(abs(t[i]-O_salida[i]))
		#prom+=error[i]
		if(error[i]<=tol):
			aciertos=aciertos+1 
		

	print("epoch #%d aciertos = %d promedio = %f"%(cont,aciertos,stats.mean(error)))
	#print("O\n")
	print("O salida")
	aux = 0
	for i in range(len(O_salida)):
		if((O_salida[i] == 0.0) or (O_salida[i] == 1.0)):
			aux+=1
		print("%f"%(O_salida[i]))	
		
	print("Error")
	for i in range(len(O_salida)):
		print("%f"%(error[i]))
	print("-------------------")

	if(aux == 4):
		break
	
	
	#O_salida.clear();
	error.clear();
	cont+=1
	