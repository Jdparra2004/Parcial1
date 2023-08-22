'''
Solución Problema 1 - Quiz y Parcial

Created on Agust 22 at 6:12 am

@authot: Juan David Parra Cantor

'''

import numpy as np 
#variables y datos
n = 0
v = np.array([1, 7, -5, 0, 7, 2, 9, 7])
vector = []

for i in range(0, len(v)):
    if v[i] == n:
        vector.append(i)
    print(f"El número n = {n}, se encuentra en la posición {vector}")
    print(f"El número n = {n}, está en el vector {len(vector)} posiciones")
else:
    print(f"El número n = {n}, no se encuentra en el vector")




