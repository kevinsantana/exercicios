# -*- coding: UTF-8 -*-
#Crie uma função que calcule o número primo seguinte ao numero
#informado.
def eh_primo(numero):
	if numero in(0,1):
		print("Existe uma grande discussao no meio academico se estes numeros sao ou nao primos, logo, aqui serao indefinidos")

	elif numero != 2 and numero % 2 == 0:		
		return False
	else:
		for numero_anterior in range(2, numero + 1):
			if numero % numero_anterior == 0 and numero_anterior != numero:				
				return False
				break
			if numero % numero_anterior == 0 and numero_anterior == numero:				
				return True
				break

def proximo_primo(numero):
	flag_encontrou_primo = False
	while flag_encontrou_primo == False:
		numero = numero + 1
		
		if eh_primo(numero) == True:
			flag_encontrou_primo = True
			return numero