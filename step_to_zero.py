#define a function if number is Even then divide by 2 else subtract by 1. continue the process till number become 0. 
#finally count the steps/iteration taken to become ZERO.
#Input number is in form of binary string. 


#Converting binary string into decimal number
def binary_to_decimal(s):
    dec = 0
    for i,x in enumerate(s[::-1]):
        if int(x) == 1:
            dec = dec+2**i
    return dec

def step_to_zero(s):
    count = 0
    n = binary_to_decimal(s)#Calling binary to decimal function to get number
    while n>0:
        if n%2==0:
            n = n//2
        else:
            n = n-1
        count +=1
    return count

step_required = step_to_zero("011100") #28
print(step_required)
