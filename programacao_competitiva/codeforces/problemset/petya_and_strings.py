# entrada, entrada1 = [ord(letra) for letra in input().lower()], [ord(letra) for letra in input().lower()]
# if sum(entrada) == sum(entrada1):
#     print(0)
# elif sum(entrada1) > sum(entrada):
#     print(-1)
# else:
#     print(1)

entrada, entrada1 = input().lower(), input().lower()
if entrada < entrada1:
    print(-1)
elif entrada == entrada1:
    print(0)
else:
    print(1)