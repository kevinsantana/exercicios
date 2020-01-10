'''
6. Write a Python program which accepts a sequence of comma
-separated numbers from user and generate a list and a tuple 
with those numbers.
'''
entrada = str(input("Informe os numeros separados por virgulas:"))
lista = entrada.split(',')
tupla = tuple(lista)
print("Lista: ", lista)
print("Tupla: ", tupla)