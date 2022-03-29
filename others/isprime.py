import math 

def isPrime(x)

    n = abs(int(x))
    
    if n < 2:
        return False
    elif n == 2:
        return True
    for element in range(2,n):
        if n%element == 0:
            return False
    return True     
        
    
