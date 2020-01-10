'''
8. Write a Python program to find missing numbers from a list.
Input : [1,2,3,4,6,7,10]
Output : [5, 8, 9]
'''

entrada = sorted([1,2,3,4,6,7,10])
lista_arrumada = [numero for numero in range(entrada[0], entrada[-1] + 1)]
numero_safado = sorted(list(set(lista_arrumada) - set(entrada)))
print(numero_safado)