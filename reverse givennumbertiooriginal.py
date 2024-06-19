def reversee(n):
    k=n
    sum=0
    while k!=0:
        r=k%10
        sum=(sum*10)+r
        k=k//10
    if n==sum:
        return sum
    else:
        return reversee(n+sum)
print("enter the number:")
a=int(input())
x=reversee(a)
print(x)