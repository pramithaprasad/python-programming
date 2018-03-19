s=int(input("number"))
if (s>0):
 for i in range(2,s):
        if (s%i==0):
          print("not a prime number")
          break
  else:
          print("prime number")
else:
   print("neither prime nor composite number")    




