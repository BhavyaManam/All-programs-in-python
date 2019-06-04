from math import sqrt,floor


def isfactor(dividend,divisor):
    if dividend % divisor==0:
        return True
    return False
def isprime(n):
    for i in range(2,n//2 + 1):
        if isfactor(n,i):
            return False
    return True
def genprimes(k):
    primecounter=0
    seqcounter=2
    while primecounter < k:
        if isprime(seqcounter):
            print(seqcounter)
            primecounter+=1
        seqcounter+=1