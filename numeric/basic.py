def power(a,n):
    if n==0:
        return 1
    else:
        return a * power(a,n-1)
    
    
def DivisibilityCheck(n):
    if (n % 9==0 and n % 11==0) and (n % 10 !=0):
        return True
    else:
        return False