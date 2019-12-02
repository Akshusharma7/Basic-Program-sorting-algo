



string = "It is Pleasent day today haveaniceday"
string_arr = string.split(' ')
string_len = [len(word) for word in string_arr]
#print(string_len)
#string_arr[string_len.index(8)]

even = 0
for i in range(len(string_len)):
    if string_len[i]%2 == 0:
        if string_len[i] > even:
            even = string_len[i]
print("Even : ",even)
index= string_len.index(even)
print("Word is : ", string_arr[index])


