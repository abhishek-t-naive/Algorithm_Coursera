# Karatsuba multiplication implementation in python

import numpy as np
import sys

# x = 10^(n/2)*a + b and y = 10^(n/2)*c + d
# x.y = 10^n*(ac) + 10^(n/2)*(ad + bc) + bd
# now recursively compute ac, ad, bc and bd

sys.setrecursionlimit(15000)

def algo_recurs(val1, val2):
	# Assuming that the length of both the multiplier and multiplicand is same
	# Currently employing numbers which are of length 2^n
	n = len(str(val1))			# n = 4
	print(n)
	divVal	= 10**(n/2)
	a = val1 / divVal			# a = 12
	b = val1 % divVal			# b = 34
	c = val2 / divVal			# c = 43
	d = val2 % divVal			# d = 21
	# let the example case be 1234 * 4321
	
	if(len(str(val1)) == 2):
		prob1 = a * c
		prob2 = b * d
		prob3 = (a+b)*(c+d) - prob1 - prob2
		finalResult = prob1*(divVal*divVal)+prob3*divVal+prob2
		return(finalResult)
	else:
		prob1 = algo_recurs(a,c)
		prob2 = algo_recurs(b,d)
		prob3 = algo_recurs((a+b),(c+d)) - prob1 -prob2
		finalResult = prob1*(divVal*divVal)+prob3*divVal+prob2
		#print(finalResult)
		return(finalResult)


#Enter the inputs

multiplicand	= input("Enter the multiplicand:")
multiplier		= input("Enter the multiplier:")
output = algo_recurs(multiplicand, multiplier)	
print(output)
