n=int(input("enter any number"))
for i in range(0,n):
  for j in range(0,n):
    if j==n-i or (i==n-1 and j!=0):
      print("*",end=" ")
    else:
      print(" ", end=" ")
  for j in range(0,n):
    if i==j or (i==n-1 and j!=n) :
      print("*",end=" ")
    else:
      print(" ", end=" ")
  
  print(end="\n")   
  
  

