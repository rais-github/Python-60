d={}
x=int(input())
for i in range(x):
    k=int(input())
    v=int(input())
    d.update({k:v})
print(d)
k_new=int(input("enter the new key:"))
v_new=int(input("enter the new value:"))
d.update({k_new:v_new})
print(d)
