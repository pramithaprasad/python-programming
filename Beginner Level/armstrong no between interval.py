n1=int(input("enter the number 1"))
n2=int(input("enter the number 2"))
for i in range(n1,n2+1):
    s=len(str(i)) 
    temp=i
    sum=0
    while(i>0):
       dig=i%10
       sum=dig**s+sum
       i=i//10
    if (temp==sum):
       print(temp)
