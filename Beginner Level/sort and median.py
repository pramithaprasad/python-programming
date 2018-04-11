n=[]
b=int(input("enter the number"))
for i in range(b):
    f=int(input("enter the value"))
    n.append(f)
n.sort()
print(n)
x=b//2
print(n[x])
