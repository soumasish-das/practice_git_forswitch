x=int(input("Enter the number"))
new=1
for i in range(2,x+1):
    new=x/i
    if (type(new)!=float):
        print(i)
    else:
        print("no divisor")