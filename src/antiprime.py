## contar el nombre de divisors positius d'un nombre enter (x)
## i: nombre per provar si és divisor de x:
## r: contar quants divisors té x:
## mentres i sigui més petit o igual a x
## si x es divisible per i, el residu es 0. si és cert, i es divisor de x
## si i és divisor de n, es suma el contador r
## incrementa i per provar el següent nombre
## r tindrà el valor total de divisors de x
def divisorsx(x):
	i = 1
	r = 0
	while i <= x:
		if x % i == 0:
			r = r + 1
		i = i + 1
	return r

## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	r = divisorsx(x)
	l = x - 1
	s = 0

	while l > 0:
		a = 1
		s = 0
		while a <= l:
			if l % a == 0:
				s = s + 1
			a = a + 1
		if s >= r:
			return ("not anti-prime")
		l = l - 1
	return("anti-prime")

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys
	x = int (sys.argv [1])
	print(main(x))

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT