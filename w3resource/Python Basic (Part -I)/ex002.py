'''
2. Write a Python program to check if a given positive integer is a power of three.
Input : 9
Output : True
'''

import math


a, x = 3, 9
# logb N = ln(N)/ln(b) # loga b = x <> a^x = b
print(True) if a**int(math.log(x)/math.log(a)) == x else print(False)