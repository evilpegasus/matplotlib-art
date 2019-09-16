from time import sleep

#Some Fibonacci Thing
def fib(n):
	if n==1:
		return 1
	if n==2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

while 0:
	n=input("Fib(n)")
	n=int(n)
	print(fib(n))

n=1
while 0:
	print("fib(" + str(n) + ") = " + str(fib(n)))
	n = n+1
	
#Faster way
if 1:
	a=1
	b=1
	f=1
	n=1
	print("fib(" + str(n) + ") = " + str(f))
	n=2
	print("fib(" + str(n) + ") = " + str(f))
	while 1:
		f=a+b
		n=n+1
		print("fib(" + str(n) + ") = " + str(f))
		a=f
		f=a+b
		n=n+1
		print("fib(" + str(n) + ") = " + str(f))
		b=f
		#sleep(3)
		