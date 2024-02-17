n=int(input("enter value"))
a=str(input("enter your smybol"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (j==(n)) or (i==j and i>=n//2) or (j==n-i and i>=n//2):
            print(a,end=" ")
        else:
            print(" ",end=" ")
    print(end="\n")       
