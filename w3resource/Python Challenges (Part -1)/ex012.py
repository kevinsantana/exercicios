'''
12. Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5
'''

entrada = [5, 3, 4, 3, 4]
resultado = [numero for numero in entrada if entrada.count(numero) <= 1].pop()
print(resultado)
