'''
Solución Parcial 1

Created on Agust 22 at 6:09 am

@Author: Juan David Parra

'''

#Problema 3

import math
import matplotlib
import numpy as np

#Tener en cuenta que la frunción corresponde a una serie de Taylor


def exponencial(x):
    n = 3
    sumatoria = 0
    
    for n in range(0, n, 1):
        sumatoria +=  math.pow(x,n) / math.factorial(n)
    return sumatoria
print(f"El resultado con la función exponencial es {exponencial(2)}")
print(f"El resultado con la función math.exp es {math.exp(2)}")

