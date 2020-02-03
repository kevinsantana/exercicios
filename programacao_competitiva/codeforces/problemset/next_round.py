n, k = map(int, input().split())
scores = list(map(int, input().split()))
if sum(scores) == 0: # a pontuacao de todos e zero
    print(0)
elif len(scores) - scores.count(0) == 1: # um elemento diferente de zero e nao e o k
    print(1)
else:
    next_round = [contest for contest in scores if contest >= scores[k - 1]]    
    print(len(next_round))