



coins = int(input("Enter the coins : "))#5 --> 2
temp = coins
for row in range(1,coins):
    
    if temp >= row:
        temp = temp - row
        print('* '*row)
    else:
        break
print("Possible row is : ",row-1 )
