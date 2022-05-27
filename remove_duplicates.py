d={}
x=int(input())
for i in range(x):
    k=int(input())
    v=int(input())
    d.update({k:v})
temp=[]
org=dict()
for key,val in d.items():
    if val not in temp:
        temp.append(val)
        org[key]=val
print(org)
