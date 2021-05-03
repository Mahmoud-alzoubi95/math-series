
#test for test
a=6


# fibonacci test
def fibonacci(n):
    if n < 0:
        pass
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# fibonacci test
def locus(n):
    if n < 0:
        pass
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    return locus(n-1) + locus(n-2)


# sum test 
def sum(n,a=0,b=1):
    if n < 0:
        pass
    elif n == 0:
        return a
    elif n == 1:
        return b

    return sum(n - 1,a,b) + sum(n - 2,a,b)

print(sum(3,2,1))        




