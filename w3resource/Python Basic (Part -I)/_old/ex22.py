'''
22. Write a Python program to count the number 4 in a given list.
'''

lista = [1,2,4,8,16,4,32,5645,4564545,4,588,4]
qtd_quatro = 0
for numero in lista:
	if numero == 4:
		qtd_quatro += 1
print(qtd_quatro)