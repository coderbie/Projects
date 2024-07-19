def binary_to_decimal(binary):
    '''
    Converts binary to decimal. 10010.101 -> 18.625
    '''
    binary_str = str(binary)
    whole_part, fractional_part = binary_str.split('.')

    number_whole_part = 0
    number_fractional_part = 0

    power = len(whole_part)-1
    for i in whole_part:
        number_whole_part += int(i)*(2**power)
        power -=1
    
    power = -1
    for j in fractional_part:
        number_fractional_part +=int(j)*(2**(power))
        power -=1
    
    return number_whole_part+number_fractional_part

def decimal_to_binary(decimal):
    '''
    Converts decimal to binary. 18.625 -> 10010.101
    '''
    decimal_str = str(decimal)
    whole = int(decimal_str.split('.')[0])
    frac = int(decimal_str.split('.')[1])/(10**len(decimal_str.split('.')[1]))

    binary_whole = ''
    binary_frac = ''

    while whole > 0:
        binary_whole+=str(whole%2)
        whole = whole//2
    binary_whole=binary_whole[::-1]

    while True:
        binary_frac+=str(int(frac*2))
        print(binary_frac)
        frac = int((str(frac*2)).split('.')[1])/(10**len((str(frac*2)).split('.')[1]))

        if frac <=0:
            break

    binary = binary_whole+"."+binary_frac

    return binary
