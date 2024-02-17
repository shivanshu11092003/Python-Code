r=9
c=10
for i in range(1,r+1):
    for j in range(1,c+1):
        if j%2==0:
            print(j*j,end=" ")
        else:
                print(j*j*j,end=" ")
    print(end="\n")
