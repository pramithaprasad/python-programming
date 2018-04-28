a=(input("enter the number"))
d=0
s=0
for i in a:
    if(i.isdigit()):
        d=d+1 
    else:
        s=s+1 
p=s+d        
if(p>0):
    print("yes")
else:
    print("no")
