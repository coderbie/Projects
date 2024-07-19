
def is_prime(n):
    '''
    Checks if a number is prime or not
    '''
    if n <=1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**(1/2)+1)):
        if n%i == 0:
            return False
    return True

def give_primes(n):
    '''
    Gives list of n prime numbers
    '''
    primes = []
    for i in range(n+1):
        if is_prime(i):
            primes.append(i)
    return primes
