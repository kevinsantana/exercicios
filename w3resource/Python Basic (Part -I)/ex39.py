'''
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, 
and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
https://www.investopedia.com/terms/f/futurevalue.asp
'''
valor = 10000
crescimento = 3.5
anos = 7
future_value = valor * ((1 + (crescimento * 0.01))**anos)
print(future_value)