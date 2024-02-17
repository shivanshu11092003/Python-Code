for n in range(5,50):
    for i in range(2,n//2+1):
        f=0
        if n%i==0:
            f=1
        if f==0:
            print(n,"p")
        else:
            print(n,"np")
    
