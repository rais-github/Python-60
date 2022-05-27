principle=int(input("Enter the principal:"))
rate=int(input("Enter the rate:"))
time=int(input("Enter the time:"))
A = principle * (((1 + rate/100))**time)
CI= A - principle
print("Compound interest is", CI)




