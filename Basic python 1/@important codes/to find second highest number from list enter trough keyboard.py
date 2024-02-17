n=list(eval(input("enter number to make form of list")))
print(n)
n.sort(reverse=True)
print("second largest number of list:",n[1])
print("largest number of list:",n[0])
z=sum(n)
print("sum of elemens is",z)

k=len(n)
mean=z/k
print("mean of list:",mean)
a=int(input("enter any numbr"))
for i in range(1,99999990):
    if a in n:
        
        print("true")
        break
    else:
        print("false")
        break

