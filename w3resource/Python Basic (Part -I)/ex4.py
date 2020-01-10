#4. Write a Python program which accepts the radius of a circle from the user and 
#compute the area.
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504
import math

raio_circulo = float(input("Informe o raio do circulo: "))
area_circulo = (math.pi) * (math.pow(raio_circulo, 2))
print("A: ", area_circulo)