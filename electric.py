print("enter the comsumption rate:")
crate=float(input())

if crate <=200:
    amount=crate * 0.50
elif crate >=201 and crate <=400:
    amount = (crate*0.50)+((crate-200)*0.65)
else:
    amount = (crate*0.50)+(crate*0.65)+((crate-400)*1.00)

if amount>400:
    print("amount: ",amount+(amount*0.15))
elif amount<100:
    print("amount: 100")
else:
    print("amount:",amount) 