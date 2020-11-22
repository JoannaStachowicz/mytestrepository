def exponent(a, b):
    if b == 0:
    	return 1
    else:
    	return a * exponent(a, b-1)
    	

print(exponent(2, 3))
