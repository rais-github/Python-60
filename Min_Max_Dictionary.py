d={}
x=int(input())
for i in range(x):
    k=int(input())
    v=int(input())
    d.update({k:v})
print(max(d.values()))
print(min(d.values()))
