for i in range(1,7):
    for j in range(1,7):
        if i==1 or j==1 or i==6 or j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end="\n")       
