a=(input("enter the number"))
d=0
s=0
for i in a:
    if(i.isdigit()):
        d=d+1 
    else:
        s=s+1 
if(d>0 and s>0):
    print("yes")
else:
    print("no")
