n=int(input("enter a no "))
for i in range(1,n+1):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    for k in range(1,i):
        print("*",end=" ")    
        
        
    print()    
    
