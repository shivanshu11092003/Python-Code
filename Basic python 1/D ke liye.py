n=int(input("ENTER YOUR VALUES"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==1 or j==n or i==n or i==1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")
    
