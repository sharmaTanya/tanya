# Python program to 
# swap bits in a given number 

def swapBits(x, p1, p2, n): 

	# Move all bits of first 
	# set to rightmost side 
	set1 = (x >> p1) & ((1<< n) - 1) 

	# Moce all bits of second 
	# set to rightmost side 
	set2 = (x >> p2) & ((1 << n) - 1) 

	# XOR the two sets 
	xor = (set1 ^ set2) 

	# Put the xor bits back 
	# to their original positions 
	xor = (xor << p1) | (xor << p2) 

	# XOR the 'xor' with the 
	# original number so that the 
	# two sets are swapped 
	result = x ^ xor 

	return result 
	
# Driver code 

res = swapBits(28, 0, 3, 2) 
print("Result =", res) 

# This code is contributed 
# by Anant Agarwal. 
