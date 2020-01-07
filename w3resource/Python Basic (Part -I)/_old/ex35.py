'''
35. Write a Python program that will return true if the two given integer values are equal or their sum or 
difference is 5.
'''
x = 8
y = 8
if x == y:
	print(True)
elif x + y == 5 or abs(x - y) == 5:
	print(True)
else:
	print(False)