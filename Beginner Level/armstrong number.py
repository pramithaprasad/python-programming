n1=int(input("enter the number"))
s1=len(str(n1))
temp=n1
sum=0
while(n1>0):
  dig=n1%10
  sum=dig**s1+sum
  n1=n1//10
if (temp==sum):
  print("armstrong number")
else:
  print(" not a armstrong number")
