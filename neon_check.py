num=int(input("Enter the number:"))
s=0
sqr=num**2
while(sqr!=0):
    s=s+sqr%10
    sqr//=10
if(s==num):
    print("the number entered is neon:")
else:
    print("The number enterd is not a neon number")