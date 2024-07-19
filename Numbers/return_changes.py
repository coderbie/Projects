def return_changes(cost: float, amount: float):
    '''
    Calculates numbers of quarters, dimes, nickels, pennies to be given as changes
    '''
    coins = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

    if cost >= amount:
        return coins
    
    changes = amount-cost
    fractional_part = round((changes-int(changes))*100)

    coins['quarters'] = round((int(changes))//0.25)
    coins['quarters'] += round((fractional_part)//25)
    coins['dimes'] = round(((fractional_part)%25)//10)
    coins['nickels'] = round((((fractional_part)%25)%10)//5)
    coins['pennies'] = round((((fractional_part)%25)%10)%5)
    
    return coins
