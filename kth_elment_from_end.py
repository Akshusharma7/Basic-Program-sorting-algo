arr = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]
k = 5

def last_elem(arr):
    p = 0
    q = k-1
    
    for i in range(100):
        p +=1
        q +=1
        if q == len(arr):
            break
    #print("element is : ", arr[p-1])
    return arr[p-1]

last_elem(arr)
