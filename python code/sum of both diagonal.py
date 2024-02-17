import numpy as np
a=np.array([[1,4,8,3,7],[8,5,8,2,8],[3,8,6,9,0],[8,3,9,4,1],[5,5,5,5,5]]).reshape(5,5)
b=a.shape
r=b[0]
c=b[1]
print(a)
s=0
d=0
for i in range(r):
  for j in range(c):
    if i==j:
      s=s+a[i][j]
      
    elif i==(r-(j+1)):
      d=d+a[i][r-(j+1)]
      print(d,"_____",a[i][r-(j+1)])
n=s+d
print("sum of both diagonal",n)
      
      
      
