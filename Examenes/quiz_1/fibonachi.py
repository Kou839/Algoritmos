def caso1(n):

    if n < 2:
        return n
    else:
        return caso1(n-1) + caso1(n-2)
    
def caso2(n):
    if n < 2:
        return n
    else:
        a=0
        b=1
    for l in range(2,n+1):
        c=a+b
        a=b
        b=c