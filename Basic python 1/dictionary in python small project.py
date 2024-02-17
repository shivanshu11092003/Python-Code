d={}
n=int(input("Enter no of times you enter:  "))
for i in range(0,n):
    companyname=str(input("Enter Your companyname :  "))
    m1=(input("Enter Your model name:  "))
    p1=int(input("Enter the price of first model:  "))
    m2=(input("Enter Your model name:  "))
    p2=int(input("Enter the price of second model:  "))
    m3=(input("Enter Your model name:  "))
    p3=int(input("Enter the price of third model:  "))
    m4=(input("Enter Your model name:  "))
    p4=int(input("Enter the price of fourth model:  "))
    d.update({companyname:
              {m1:{"price":p1},
              m2:{"price":p2},
              m3:{"price":p3},
              m4:{"price":p4}}})
    print(d)

        
        

    
