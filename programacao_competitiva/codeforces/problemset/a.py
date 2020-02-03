# -*- coding: utf-8 -*-
# entrada = input().split(' ')
# entrada.sort()
# x4 = int(entrada.pop(-1))
# x3 = int(entrada.pop(2))
# x2 = int(entrada.pop(1))
# x1 = int(entrada.pop(0))
x1,x2,x3,x4 = 201,101,101,200
# Todas diferentes
if x1 != x2 != x3 != x4:
	a = x4 - x3
	b = x4 - x2
	c = x4 - x1
	print("todas diferentes")
	print(a,b,c)
# Tres entradas iguais
elif x1 != x2 or x1 != x3 or x1 != x4:
	a = x4 - x3
	b = x4 - x3
	c = x4 - x3
	print("tres iguais")
	print(a,b,c)
# Duas entradas iguais
elif ((x1 == x2) and (x1 == x4) or (x2 == x3) and (x2 == x4)):
	a = x4 - x3
	b = x4 - x2
	c = x4 - x1
	print("duas iguais")
	print(a,b,c)
# Todas as entradas iguais
elif (x1==x2==x3==x4) and (x4==x2==x3==x1):
	a = x1
	b = x1
	c = x1
	print("todas iguais")
	print(a,b,c)
else:
	print("erro")

'''
receber os numeros, colocar em uma lista e ordenar os numeros
n = list(map(int, input().split())
n = sort()
print("a:", n[0]-n[1])

'''