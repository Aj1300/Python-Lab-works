print("enter the 1st no: ")
x=int(input())
print("enter the 2nd no: ")
y=int(input())
print("option")
print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.divide")
print("enter your option")
o=int(input())
if o==1:
    print("result",x+y)
elif o==2:
    print("result",x-y)
elif o==3:
    print("result",x*y)
elif o==4:
    if(y!=0):
        print("result",x/y)
    else:
        print("0 cant be used for dividing")
else:
    print("wrong input")
