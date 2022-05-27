def fib():
    n=int(input())
    if(n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))
    for i in range(n):
        if(n==0):
            print("Please enter positve  number:")
        else:
            print(fib(i))

f=map(lambda )