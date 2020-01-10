'''
26. Write a Python program to create a histogram from a given list of integers.
'''
from collections import Counter
dados = [1,3,5,7,9,11,13,17,19,23,27,1,5,7,13,17,5,27,27,11,13,13,13]
histograma = {x:dados.count(x) for x in dados}
conta_histograma = "*"
for x,y in histograma.items():
	print(x, ":", y*conta_histograma , sep="")