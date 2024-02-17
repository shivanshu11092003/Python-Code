n=str(input("enter a string")) #manu
l=len(n) #4
m=""
for i in range(0,l,2):
  m+=n[i]  #m=m i=0
  print(m) 
  if i<(l-1): #0<4-1
    m+=n[i+1].upper() #m=m+ i=0
    print(m)
  

  
