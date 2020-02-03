# import math
# n, m, a = map(int, input().split(" "))
# print(1) if a**2 > n * m else print(int((n * m) / a**2)) if (n * m) % a**2 == 0 else print(int((math.ceil((n * m) / a**2)) + 1))

import math
n, m, a = map(int, input().split())
if (n * m) % a ** 2 == 0:
    print((n * m) // a ** 2)
elif (n * m) == a ** 2 or (a ** 2) > (n * m) or n == m == a or n == m == a == 1:
    print(1)
elif (n * m) % a ** 2 != 0:
    print(math.ceil((n * m) / a ** 2) + 1)