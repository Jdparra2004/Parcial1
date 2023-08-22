'''
Solución Problema 1 - Quiz y Parcial

Created on Agust 22 at 6:12 am

@authot: Juan David Parra Cantor

'''
#Variables
n = 5
a = 0
b = 1
c = 2


suma = a + b
i = 0
while (i<= n):
    c = a + b
    suma += c
    a, b = b, a
    c, b = b, c     
    i += 1
print(f"Los resultados obtenidos son: a = {a}, b = {b}, c = {c}, suma = {suma}")
