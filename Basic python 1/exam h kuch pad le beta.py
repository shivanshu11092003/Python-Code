n=int(input("enter a no number"))
print(1,end=" ")
l=[]
for i in range(1,n+1):
    m=i+0
    print(m,end=" ")
    l.append(m)
    i+=1
print()    
print(l)
print(sum(l)+1)
