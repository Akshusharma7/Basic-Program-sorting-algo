




string = "I am using HackerRank to improve programming"
sub = "am HackerRank to improve"

string_arr = string.split(' ')
sub_arr = sub.split(' ')

for ind in range(len(sub_arr)):
    if sub_arr[ind] in string_arr:
        #print(sub_arr[ind])
        index = string_arr.index(sub_arr[ind])
        remove = string_arr.pop(index)

        
print("OUTPUT 1:")
for word in string_arr:
    print(word)
    
print("OUTPUT 2:")
out = ' '.join(string_arr)
print(out)

