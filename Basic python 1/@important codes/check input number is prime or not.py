n=int(input("enter no for checking of prime number"))
if (n>1):
    for i in range(2,n):
        if n%i==0:
            print("NOT PRIME")
            break
        else:
            print("PRIME")
            break
else:
    print("in valid")
