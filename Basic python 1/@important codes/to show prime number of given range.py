s=int(input("enter no to start"))
e=int(input("enter no to end"))
l=[]
if (s>1):
    for i in range(s,e+1):
        f=0
        for j in range(2,i):
            if (i%j==0):
                f=1
                break
            if (f==0):
                print("prime:",i)
                l.append(i)
                break
                
else:
    print("not valid:")

l.sort(reverse=True)
print("new list",l)
print("maximum value",l[0])
print("minimum value:",min(l))
print("sum of number which are prime:",sum(l))


