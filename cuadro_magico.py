#import random
#import math

def orden_cuadro(n):
  return (n*(pow(n,2)+1))/2


print("SOLUCIONADOR DE CUADROS MAGICOS\n")
n = int(input("Orden del cuadro magico = ")) #tamaño del cuadro magico
mu = float(input("Mutacion = ")) #porcentaje de mutacion de cada individuo

orden = math.ceil(orden_cuadro(n));

print("Orden = %d"%(orden))

ind = []
for i in range(orden):
  ind[i] = i

print(ind)

