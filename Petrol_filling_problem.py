
#Petrol filling problem in Facebook interview. 
#Find the node from which you start the trip and complete it without shortage of petrol. time complexity should be BIG O of N


n = int(input("Enter number of Petrol pump : "))
print("Enter Petrol array")


petrol = [int(input())  for i in range(n)]
#print(petrol)

print("Enter distance array")
distance= [int(input())  for i in range(n)]
#print(distance)

#---------LOGIC-----------------
def petrol_filling(petrol, distance,n):
    total = 0
    diff = 0
    start = 0
    for i in range(n):
        total = total+petrol[i]-distance[i]

        if total<0:
            start = start+1
            diff = diff+total
            total = 0

    if diff+total>=0:
        print(petrol[start])
    else:
        print("Not able to take tour")
    
    return start

#Create an object
obj = petrol_filling(petrol,distance,n)

print("Index of Petrol is :",obj)

