# Enter your answrs for chapter 7 here
# Name:shishira


# Ex. 7.5
import math
def factorial(n):
	if n==0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n*recurse
		return result


def estimate_pi():
	x=((2*math.sqrt(2))/9801.0)
	while True:
		k=0
		f=4*k	
		y=(factorial(k)**4)*(396**f)
		n=(factorial(f))*(1103.0+(26390*k))
		pi=1.0/(x*(n/y))
		k=k+1
		if pi<1e-15:
			break
			return k
		
			
print estimate_pi()		



# How many iterations does it take to converge?