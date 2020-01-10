'''
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies
of the whole string if the length is less than 2.
'''

n = 1
frase = "space: the final frontier"
copia_frase = n * frase[:2]
print(copia_frase) if len(copia_frase) <= 2 else print()