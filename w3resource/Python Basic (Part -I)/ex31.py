'''
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''
import proximo_primo
num1 = 20
num2 = 50
aux = []
gcd = 1

for x in range(max(num1, num2)):
	aux.append(gcd)
	print("antes",num1,num2,gcd)
	num1 = num1//gcd
	num2 = num2//gcd
	print("depois",num1,num2,gcd)
	gcd = proximo_primo.proximo_primo(gcd)


print(aux)

