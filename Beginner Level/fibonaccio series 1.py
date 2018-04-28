n=int(input("enter the number"))
x=0
y=1 
for a in range(n):
    if(a<=1):
        next=a 
    else:
        next=x+y 
        x=y
        y=next
    a=a+1
print(next)
