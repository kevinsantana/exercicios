minutos_total_ano_novo, horas_ano_novo, minutos_ano_novo = list(), 0, 0
for _ in range(int(input())):
    h, m = map(int, input().split(" "))
    horas_ano_novo = (24 - h) * 60
    minutos_ano_novo = 60 - m
    if h == 0 and m == 0:
        horas_ano_novo, minutos_ano_novo = 0, 0
        minutos_total_ano_novo.append((horas_ano_novo) + minutos_ano_novo)
    else:
        minutos_total_ano_novo.append((horas_ano_novo - 60) + minutos_ano_novo)
print(*(minutos_total_ano_novo), sep="\n")
    