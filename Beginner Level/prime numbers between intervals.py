num1=int(input("number 1"))
num2=int(input("number 2"))
for a in range(num1,num2+1):
 if(a>1):
  for i in range(2,a):
   if(a%i==0):
    break
  else:
   print(a)      
