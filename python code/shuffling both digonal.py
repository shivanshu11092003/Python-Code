import numpy as np
a=np.arange(1,26).reshape(5,5)
b=a.shape
r=b[0]
c=b[1]
print(a)
for i in range(r):
  for j in range(c):
    if i==j:
      t=a[i][j]
      a[i][j]=a[i][c-(i+1)]
      a[i][c-(i+1)]=t
print(a)

