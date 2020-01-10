'''
5. Write a Python program to check if an integer is the power of another integer.
Input : 16, 2
Output : True
'''

import math


a, x = 3, 16
# logb N = ln(N)/ln(b) # loga b = x <> a^x = b
print(True) if a**int(math.log(x)/math.log(a)) == x else print(False)