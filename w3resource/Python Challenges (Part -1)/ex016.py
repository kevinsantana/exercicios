'''
16. Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5
'''


def soma_digitos(entrada: int):
    return sum([int(numero) for numero in str(entrada)])


entrada = 88886645689879879
saida = soma_digitos(soma_digitos(entrada))
print(saida)