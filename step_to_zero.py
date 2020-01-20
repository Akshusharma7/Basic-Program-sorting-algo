def binary_to_decimal(s):
    dec = 0
    for i,x in enumerate(s[::-1]):
        if int(x) == 1:
            dec = dec+2**i
    return dec
