st=eval(input("enter list"))
length=len(st)
mean=sum=0
for i in range(0,length):
    sum=sum+st[i]
    mean=sum/length
print("given list",st)
print("mean",mean)
