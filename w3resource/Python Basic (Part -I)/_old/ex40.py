'''
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
'''
from math import sqrt

a = (2, 3)
b = (5, 7)
distancia_euclidiana = sqrt(((b[0] - a[0])**2) + (b[1] + a[1])**2)
print(distancia_euclidiana)