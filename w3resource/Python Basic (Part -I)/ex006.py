'''
6. Write a Python program to check if a number is a power of a given base.
Input : 128,2
Output : True
'''

import math


a, x = 2, 128
# logb N = ln(N)/ln(b) # loga b = x <> a^x = b
print(True) if a**int(math.log(x)/math.log(a)) == x else print(False)