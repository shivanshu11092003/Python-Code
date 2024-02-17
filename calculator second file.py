import calculator as cal
print("for multiplication---","\t","multi","\t")
print("for division---","\t","\t""div","\t")
print("for addition---","\t","\t""add","\t")
print("for subtraction---","\t","\t""sub","\t")
def first():
  a=int(input("Enter a number"))
  b=int(input("Enter a number"))
  n=str(input("Operator Name:"))
  
  if n=="multi":
    print("Your answer is:--","\t",cal.multi(a,b),"\t")
  elif n=="div":
    print("Your answer is:--","\t",cal.div(a,b),"\t")
  elif n=="add":
    print("Your answer is:--","\t",cal.add(a,b),"\t")
  elif n=="sub":
    print("Your answer is:--","\t",cal.sub(a,b),"\t")
  else:
    print("wrong entry")
for i in range(999):
  first()  
  
