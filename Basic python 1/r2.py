n=int(input("enter"))
for i in range(0,n):
    for j in range(0,n):
        if j==0 or (j==i and i<=n//2)  or (j==(n-i) and i<=n//2) or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end="\n")        
