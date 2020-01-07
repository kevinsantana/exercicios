'''
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already 
begins with "Is" then return the string unchanged.
'''

frase = "Empty"
nova_frase = ""
nova_frase = "Is" + frase if frase.startswith("Is") != True else nova_frase.join(frase)
print(nova_frase)
