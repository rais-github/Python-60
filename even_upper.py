str=input()
l=len(str)
x=""
for i in range(l):
    if (i%2==0):
        x=x+str[i].upper()
    else:
        x=x+str[i].lower()
    
print(x)
