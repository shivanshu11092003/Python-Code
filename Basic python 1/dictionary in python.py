print("____________________________________________________________________________________________________")
d={"samsung":{"s1":{"price":12000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "s2":{"price":32000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "s3":{"price":42000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "s4":{"price":22000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"}},
   "apple":{"a1":{"price":12000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "a2":{"price":32000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "a3":{"price":42000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "a4":{"price":22000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"}},
   "nokia":{"n1":{"price":12000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "n2":{"price":32000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "n3":{"price":42000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "n4":{"price":22000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"}},
   "blackberry":{"b1":{"price":12000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "b2":{"price":32000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "b3":{"price":42000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"},
              "b4":{"price":22000,"camera_quality":"48mp","colour":"red","ram":"4gb","rom":"64gb"}}
   }
for i in range(0,10):
    comp=str(input("enter your company::: "))
    if comp in d:
        model=str(input("enter your model you want"))
        if model in d[comp]:
            detail=d[comp][model]
            print("detail of model you are buying",detail)
            price=d[comp][model]['price']
            q=int(input("enter your quantity"))
            a=price*q
            dis=0
            if a>10000:
                dis=6
            else:
                print("no discount")
            dm=a*dis/100
            netam=a-dm
            print("CALCULATED AMOUNT-------$",a)
            print("DISCOUNT AMOUNT---------$",dm)
            print("PAYABLE AMOUNT-----------$:",netam)
            print("***************************CALCULATION DONE NEXT BILL*************************************************")
        else:
            print("no such model")
            print("********************************CALCULATION DONE NEXT BILL********************************************")
    else:
        print("no such company available")
        print("********************************CALCULATION DONE NEXT BILL********************************************")
    
