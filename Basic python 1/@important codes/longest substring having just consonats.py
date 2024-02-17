s=input("enter a string :")
l=len(s)
maxl=0
maxsub=" "
sub=" "
lensub=0
for a in range(l):
    if s[a] in "aeiou" or s[a] in "AEIOU":
        if lensub>maxl:
            maxsub=sub
            maxl=lensub
            sub=" "
            lensub=0
        else:
            sub+=s[a]
            lensub=len(sub)
        a=a+1
    print(" maximum length substring is:",maxsub,end=" ")
    print("with",maxl,"character")
