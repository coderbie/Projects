def coin_flip(n: int):
    '''
    Flips a coin n times and record heads and tails.
    returns (tails, heads)
    '''
    tails = 0
    heads = 0
    for i in range(n):
        outcome = random.choice(('T', 'H'))
        if outcome == 'T':
            tails+=1
        else:
            heads+=1
    
    return (tails, heads)
