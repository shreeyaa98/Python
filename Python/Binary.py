n=int(input('Enter a number'))
b='0'
def bin(n):
	global b
	if n==0:
		if b=='0':
			return b
		else:
			b=b[-1::-1]
			b=b[:len(b)-1]
			return b

	else:
		i=n%2
		i=str(i)
		b=b+i
		return bin(n//2)

def leap(n):
	if n%4 !=0:
		return 'Not a leap year'
	else:
		if n%100==0:
			if n%400!=0:
				return "Not a leap year"
		return'Leap Year'
		

print(leap(n))
