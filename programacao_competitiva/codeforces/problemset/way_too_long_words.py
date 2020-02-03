resultado = list()
for n in range(int(input())):
    palavra = ''.join(input().split("\n")).lower()
    if len(palavra) > 10:
        abreviacao = list(palavra)
        primeira_letra, ultima_letra, qtd_letras = abreviacao.pop(0), abreviacao.pop(), len(abreviacao)
        abreviacao = f"{primeira_letra}{str(qtd_letras)}{ultima_letra}"
        resultado.append(abreviacao)
    else:
        resultado.append(palavra)
print(*resultado, sep="\n")