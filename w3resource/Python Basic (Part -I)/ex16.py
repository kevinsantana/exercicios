#16. Write a Python program to get the difference between a given number 
#and 17, if the number is greater than 17 return double the absolute 
#difference.
x = int(input("E ai fake: "))
if x < 17:
	ans = x - 17
else:
	ans = 2 * abs(x - 17)
print(ans)