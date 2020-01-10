'''
33. Write a Python program to compute the sum of all the multiples of 3 or 5 below 500. 
All the natural numbers below 12 that are multiples of 3 or 5, we get 3, 5, 6, 9 and 10. The sum of these 
multiples is 33.
'''
ate_500 = list(range(0,500))
multiplos = sum([x for x in ate_500 if x % 3 == 0 or x % 5 == 0])
print(multiplos)