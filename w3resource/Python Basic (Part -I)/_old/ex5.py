#5. Write a Python program which accepts the user's first and last name and print 
#them in reverse order with a space between them.

#nome = "Kevin de Santana Araujo"
nome = input("Informe nome e sobrenome: ")
nome_sobrenome = nome.rsplit(" ") #divide o nome informado a cada espaco vazio
sobrenome_aviao = nome_sobrenome[len(nome_sobrenome) - 1]
nome_aviao = nome_sobrenome[0]
nome_sobrenome_aviao = sobrenome_aviao + " " + nome_aviao
print(nome_sobrenome_aviao)