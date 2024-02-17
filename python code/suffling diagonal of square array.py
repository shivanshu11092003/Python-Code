import numpy as np
a=np.arange(25).reshape(5,5)
print("ARRAY")
print(a)
z=a.shape
r=z[0]
c=z[1]
s=int((r+1)/2)
for i in range(s):
  for j in range(c):
    if i==j:
      t=a[i][j]
      a[i][j]=a[r-1-i][r-1-i]
      a[r-1-i][r-1-i]=t
      
print("__________Diagonal shuffling__________")
print(a)
      
