m1=int(input("enter the 1 subjuct marks: "))
m2=int(input("enter the 2 subjuct marks: "))
m3=int(input("enter the 3 subjuct marks: "))
a=m1+m2+m3
tp = ((a*100)//300)
if(tp > 33):
    print("you are pramoted")
else:
    print("not pramoted")
