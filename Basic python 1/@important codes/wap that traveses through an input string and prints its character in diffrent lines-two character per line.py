n=str(input("enter a string"))
l=len(n)
if l%2==0:
  for i in range(0,l,2):
    print(n[i],n[i+1])
else:
  m=n+" "
  for i in range(0,l,2):
    print(m[i],m[i+1])
  
