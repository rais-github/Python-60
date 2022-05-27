d={}
x=int(input())
for i in range(x):
    k=int(input())
    v=int(input())
    d.update({k:v})
k=int(input())
if k in d: 
    del d[k]
else:
    print("Key not found!")
print(d)
