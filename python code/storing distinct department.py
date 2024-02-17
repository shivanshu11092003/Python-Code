name=["ajay","abhinash","aniket","vijay"]
desi=["clerk","manager","operator","operator"]
salary=[47000,87000,70000,20000]

import pandas as pd
data={"name":name,"desin":desi,"salary":salary}
emp=pd.DataFrame(data=data)
l=[]
for (i,j) in emp.iteritems():
  m=len(j)
  for x in range(m):
    if i=="desin":
      n=j[x]
      if n not in l:
        l.append(n)
print(l)

    
    
      
      
      
      
  
    
