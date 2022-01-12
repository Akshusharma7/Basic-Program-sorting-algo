"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

"""

def longest_substring_with_k_distinct_characters(character,k):

    current_length = ''
    for i in range(len(character)):
        for j in range(i+1,len(character)+1):
            substring = character[i:j]
            if len(set(substring)) <= k and len(substring) > len(current_length):
                current_length = substring
    return current_length
    

if __name__ == '__main__':
    s = "abcba"
    k = 2
    out = longest_substring_with_k_distinct_characters(s,k)
    print(out)

   

    

  
