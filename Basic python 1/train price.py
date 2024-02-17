d={
    1001: {
        'train_name': 'Jablpur express',
        'first class fare': 1000,
        'second class fare': 700,
        'third class fare': 500,
        'general seat fare': 100},
    1002:
    {'train_name': 'ExpressB',
     'first class fare': 1200,
     'second class fare': 1100,
     'third class fare': 1000,
     'general seat fare': 500},
    1003:
    {'train_name': 'ExpressC',
     'first class fare': 1500,
     'second class fare': 1200,
     'third class fare': 1000,
     'general seat fare': 500},
    1004:
    {'train_name': 'ExpressD',
     'first class fare': 1100,
     'second class fare': 900,
     'third class fare': 500,
     'general seat fare': 300}}
print(d)
print("_________________________________________________________________")
for i in range(0,999999):
    a=str(input("enter train name::"))
    b=int(input("Enter train number"))
    if b in d:
        cls=str(input("Enter str class"))
        if cls in d[a]:
            price=d[a][cls]
            noseats=int(input("Enter No of seat book int"))
            amount=price*noseats
            k=int(input("discount:"))
            dis=amount*k/100
            net=amount-dis
            print("train name",a)
            print("train number",b)
            print("class name",cls)
            print("no of seats are booked",noseats)
            print("AMOUNT",amount)
            print("discount of %",k)
            print("net payable amount",net)
        else:
            print("no available")
    else:
        print("no such train")
        
        
        
       
