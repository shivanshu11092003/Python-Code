d={}
n=int(input("Enter no of times you enter:  "))
for i in range(0,n):
    train_no=int(input("Enter Your Train No:  "))
    train_n=str(input("Enter Your Train Name:  "))
    cls1=int(input("Enter Your cls1 No:  "))
    cls2=int(input("Enter Your cls2 No:  "))
    cls3=int(input("Enter Your cls3 No:  "))
    gn=int(input("Enter Your gn No:  "))
    d.update({train_no:{"train_name":train_n,"first class fare":cls1,"second class fare":cls2,"third class fare":cls3,"general seat fare":gn,}})
    print(d)
    

    
