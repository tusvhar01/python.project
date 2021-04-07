a=int(input("enter the 1 no.: "))
b=int(input("enter the 1 no.: "))
c=int(input("enter the 3 no.: "))
d=int(input("enter the 4 no.: "))
if(a>d):
    f1=a
else:
    f1=d
    if(b>c):
        f2=b
    else:
        f2=c
        if(f1>f2):
            print("greatest",f1)
        else:
            print("greatest,f2")