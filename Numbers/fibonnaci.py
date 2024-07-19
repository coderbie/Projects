
def fibonnaci(n):
    '''
    Gives the nth number in fibonnaci series
    '''
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    return fibonnaci(n-1)+fibonnaci(n-2)

def fibonnaci_list(n):
    '''
    Gives the list n fibonnaci numbers
    '''
    numbers = []
    index = 0
    while True:
        numbers.append(fibonnaci(index))
        index+=1
        if index >range:
            break
    
    return n
