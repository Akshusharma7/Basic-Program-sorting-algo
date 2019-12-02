#HackerRank problem
#Count the number of row possibe after aranging the coins in shape of stairs.
#suppose there are 5 coins then possible stairs will be 2 and if there are 15 coins the stairs will be 5.



coins = int(input("Enter the coins : "))#5 --> 2
temp = coins
for row in range(1,coins):
    
    if temp >= row:
        temp = temp - row
        print('* '*row)
    else:
        break
print("Possible row is : ",row-1 )
