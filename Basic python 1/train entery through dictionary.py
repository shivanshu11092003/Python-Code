d={}
n=int(input("Enter no of times you enter:  "))
for i in range(0,n):
    trainno=int(input("Enter Train Number:  "))
    tname=str(input("Enter Your Train name :  "))
    c1=(input("Enter Your class :  "))
    p1=int(input("Enter the price of class:  "))
    c2=(input("Enter Your class:  "))
    p2=int(input("Enter the price of class:  "))
    c3=(input("Enter Your class:  "))
    p3=int(input("Enter the price of class:  "))
    c4=(input("Enter Your class:  "))
    p4=int(input("Enter the price of class:  "))
    d.update({trainno:{tname:
              {c1:{"price":p1},
              c2:{"price":p2},
              c3:{"price":p3},
              c4:{"price":p4} }}})
    
    print(d)
