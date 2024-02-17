name=input("enter string")
length=len(name)
i=0
for h in range(-1,(-length-1),-1):
    print(name[i],"\t",name[h])
    i=i+1
