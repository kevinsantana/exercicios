#10. Write a Python program that accepts an integer (n) and computes 
#the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

valor = str(input("Informe o numero: "))
lista = [valor, valor+valor, valor+valor+valor]
print(sum([int(x) for x in lista]))

