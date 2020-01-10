'''
9. Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
Input : [-1,0,1,2,-1,-4]
Output : [[-1, -1, 2], [-1, 0, 1]]
Note : Find the unique triplets in the array. 
'''

entrada = [-1,0,1,2,-1,-4]
somas = list()
for numero in entrada:    
    for num in range(len(entrada)-1):        
        if num + 2 > len(entrada) - 1:
            break
        soma = entrada[numero] + entrada[num+1] + entrada[num+2]
        if soma == 0:
            resultado = [entrada[numero],entrada[num+1],entrada[num+2]]
            somas.append(resultado)
print(somas)