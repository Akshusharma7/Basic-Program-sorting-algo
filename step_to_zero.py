def binary_to_decimal(s):
    dec = 0
    for i,x in enumerate(s[::-1]):
        if int(x) == 1:
            dec = dec+2**i
    return dec

def step_to_zero(s):
    count = 0
    n = binary_to_decimal(s)
    while n>0:
        if n%2==0:
            n = n//2
        else:
            n = n-1
        count +=1
    return count

step_required = step_to_zero("011100") #28
print(step_required)
