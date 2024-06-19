def recusiveF(n):
    if n!=0:
        return n +recusiveF(n-1)
    else:
        return n
x = recusiveF(10)
print(x)