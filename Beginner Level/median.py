s=[]
n=int(input("value"))
for i in range(1,n+1):
 b=int(input("numbers"))
 s.append(b)
 s.sort()
print(s)
print(s[n//2])
