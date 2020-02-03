'''
Vowels are letters "A", "O", "Y", "E", "U", "I"
'''
entrada = list(input())
saida1 = ["." + letra.lower() for letra in entrada if letra.upper() not in ("A", "O", "Y", "E", "U", "I")]
print(''.join(saida1))