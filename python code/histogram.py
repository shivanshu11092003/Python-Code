import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,2,2,3,4,2,2,4,4,3,2,4,2,2,3,4,3,1,2,3,4,2,3,2,1,1,1,3,3,2,1]
p=[0,1,2,3,4,5]
plt.hist(x)
plt.xticks(p)
plt.xlim(0,5)

l=[]
m=[]
q=[]
e=[]
for i in x:
  if i==2:
    l.append(i)
  elif i==1:
    m.append(i)
  elif i==3:
    q.append(i)
  elif i==4:
    e.append(i)
a=np.array([0,len(m),len(l),len(q),len(e),0])
plt.plot(p,a,marker="*",color="k")
plt.show()




    
    


  
