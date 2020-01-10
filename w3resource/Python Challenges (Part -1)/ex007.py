'''
7. Write a Python program to find a missing number from a list.
Input : [1,2,3,4,6,7,8]
Output : 5
'''

entrada = sorted([1,2,3,4,6,7,8])
lista_arrumada = [numero for numero in range(entrada[0], entrada[-1] + 1)]
numero_safado = set(lista_arrumada) - set(entrada)
print(*map(int, numero_safado))