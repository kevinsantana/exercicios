'''
27. Write a Python program to concatenate all elements in a list into a string and return it.
'''

lista_de_coisas = [2,"Memento", "XIII", 13, "Death"]
junta_tudo = ''.join(str(x) for x in lista_de_coisas)
print(junta_tudo)