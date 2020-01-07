#17. Write a Python program to test whether a number is within 100 of 1000 
#or 2000. 
x = 101
if x <= 100 and x > 0:
	print("entre 0 e 100")
elif x <= 1000 and x > 100:
	print("entre 101 e 1000")
elif x <= 2000 and x > 1000:
	print("entre 1001 e 2000")
else:
	print("Deu erro mane")