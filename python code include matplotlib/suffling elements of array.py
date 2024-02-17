import numpy as np
a=np.arange(25).reshape(5,5)
print("original array")
print(a)
z=a.shape
r=z[0]
c=z[1]
for i in range(r):
  for j in range(c):
    if i==0:
      t=a[i][j]
      a[i][j]=a[r-1][j]
      a[r-1][j]=t
print("array after coding")      
print(a)      
