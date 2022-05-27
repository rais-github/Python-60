
amount=int(input("Enter the amount you want to withdraw:"))

notwh=amount/2000
amount=amount%2000
nofh=amount/500
amount=amount%500
nohun=amount/100
amount=amount%100

print("Number of hundred reupee notes dispensed:",round(nohun))
print("The minimum notes that can be withdrawn are:",round(notwh+nofh+nohun))