n=int(input("enter your number"))
l=[]
for i in range(1,n+1):
    k=i*i
    i=i+1
    m=l.append(k)
print(l)
print("sum of series",sum(l))
l2=l.sort(reverse=True)
print(l)
print('greatest number is:  ',l[0])

