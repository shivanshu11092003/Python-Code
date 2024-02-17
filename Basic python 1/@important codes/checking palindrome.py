string=input("enter a string")
length=len(string)
m=int(length/2)
rev=-1
for a in range(m) :
    if string[a]==string[rev]:
        a+=1
        rev-=1
    else:
        print(string,"is not a palindrome")
        break
else:
        print(string,"is a palidrome")    
    
