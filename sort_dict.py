d={}
x=int(input())
for i in range(x):
    k=int(input())
    v=int(input())
    d.update({k:v})
print(sorted(d.values(),reverse=True))
