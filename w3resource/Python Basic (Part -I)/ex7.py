'''
7. Write a Python program to accept a filename from the user and print
the extension of that.
'''
# O ':' no final do indice, garante que a posicao sera incluida
entrada = input("Informe um arquvo com extensao(.): ")
print(entrada[entrada.find('.'):-1] + entrada[-1:])