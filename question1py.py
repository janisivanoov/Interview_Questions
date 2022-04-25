#3! =3*2*1
#n! = n *(n-1)*(n-2)...*1

factorial = 1

def factorial (number):

#number = int(input(“Number: “))

    for i in range(1, number):
        factorial = factorial * i

    return factorial

def factorial2(numb):
	return 1 if( numb == 0 or numb == 1) else numb * factorial(numb - 1)
