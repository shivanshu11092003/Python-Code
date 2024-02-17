import numpy as a
b=a.arange(20).reshape(4,5)
print(b)
c=b.shape
d=c[0]
e=c[1]
s=0
for i in range(d):
  for j in range(e):
    s=s+b[i][j]
print("sum",s)    
    
