'''
17. Write a Python program to find whether it contains an additive sequence or not.
The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
Sample additive sequence: 6, 6, 12, 18, 30
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Also, you can split a number into one or more digits to create an additive sequence.
Sample additive sequence: 66121830
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Note : Numbers in the additive sequence cannot have leading zeros.
'''

entrada = [6, 6, 12, 18, 30]
lista = list()
for numero in range(len(entrada)):
    print(numero + entrada[numero+1] == entrada[numero+2])
    if entrada[numero+2] > len(entrada):
        break
    if numero + entrada[numero+1] == entrada[numero+2]:        
        lista.append(True)
print("contem sequencia aditiva") if all(lista) else print("nao contem sequencia aditiva")