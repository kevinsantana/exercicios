retirada, conta_inicial = map(float, input().split(" "))    
print(f"{conta_inicial:.2f}") if retirada > conta_inicial or retirada % 5 != 0 else print(f"{((conta_inicial - retirada - 0.05)):.2f}")