import math

def mortgage_calc(priniciple_amt, rate: float, term, compounding_interval):
    '''
    Calculate monthly payments for a fixed term mortgage
    '''
    if priniciple_amt <= 0 or rate < 0 or rate > 1 or term <= 0:
        raise ValueError("Principal amount and term must be greater than 0, and rate must be non-negative and between 0-1.")
    
    if compounding_interval == "weekly":
        rate_monthly = ((1+(rate/52))**(52/12))-1
    elif compounding_interval ==  "monthly":
        rate_monthly = rate/12
    elif compounding_interval == "daily":
        rate_monthly = ((1+(rate/365))**(365/12))-1
    elif compounding_interval == "continually":
        rate_monthly = math.e**(rate/12) - 1
    else:
        raise ValueError("choose compounding_interval from (weekly, monthly, daily, continually)")
        
    terms_in_month = term*12
    monthy_payment = priniciple_amt*((rate_monthly*(1+rate_monthly)**terms_in_month)/(((1+rate_monthly)**terms_in_month)-1))

    return round(monthy_payment, 2)
