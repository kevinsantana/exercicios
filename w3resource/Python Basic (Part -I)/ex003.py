'''
3. Write a Python program to check if a given positive integer is a power of four.
Input : 4
Output : True
'''

import math


a, x = 4, 64
# logb N = ln(N)/ln(b) # loga b = x <> a^x = b
print(True) if a**int(math.log(x)/math.log(a)) == x else print(False)