x=int(input("enter a number: "))

for i in range(2,int(x/2)+1):

  if x%i==0:
    
    print("no")
    break
  else:
    print("prime")
    break