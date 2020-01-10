'''
24. Write a Python program to test whether a passed letter is a vowel or not.
'''

letra = "a"
print("Vogal") if ord(letra.lower()) in (97, 101, 105, 111, 117) else print("Nao e vogal")