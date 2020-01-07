#18. Write a Python program to calculate the sum of three given numbers, if 
#the values are equal then return thrice of their sum
x,y,z = 2,2,3
if x == y == z:
	print(3 * tuple(str(x + y + z)))
else:
	print(x + y + z)