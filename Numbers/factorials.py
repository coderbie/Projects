def factorial_using_loop(n):
    '''
    Calculates factorial using while loop.
    The Factorial of a positive integer, n, is defined as the product of the sequence 
    n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1.
    '''
    factorial = 1
    
    while n > 0:
        factorial *=n
        n-=1
    
    return factorial

def factorial_using_recursion(n):
    '''
    Calculates factorial using recursion
    '''
    if n < 2:
        return 1
    
    return factorial_using_recursion(n-1)*n

