'''
32. Write a Python program to find the single number which occurs odd numbers and other numbers occur even number.
'''
from collections import Counter
num1 = [4, 5, 4, 5, 2, 2, 3, 3, 2, 4, 4]
conta_num = {x:num1.count(x) for x in num1}
for k,v in conta_num.items():
	if v % 2 != 0:
		print("chave:", k ,"valor:", conta_num.get(0,v))
