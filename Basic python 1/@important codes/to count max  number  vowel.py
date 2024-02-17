n1=str(input("enter any a string"))
c1=0
c2=0
for i in n1:
    if  i=="a" or i=="u" or i=="o" or i=="i" or i=="e":
        print("vowel",i)
        c1+=1
    else:
        print("consonant",i)
        c2+=1
n2=str(input("enter any a string"))
c3=0
c4=0
for i in n2:
    if  i=="a" or i=="u" or i=="o" or i=="i" or i=="e":
        print("vowel",i)
        c3+=1
    else:
        print("consonant",i)
        c4+=1        
if c1>c3:
    print(n1,"having max vowel")
else:
    print(n2,"having max vowel")
print(n1,"contain vowel",c1)
print(n1,"contain consonant",c2)
print(n2,"contain vowel",c3)
print(n2,"contain consonant",c4)
