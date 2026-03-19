def reverse(S, i):
    if len(S) == 0 or len(S) == 1:
        return

    start = 0

    while start < i:
        temp = S[start]
        S[start] = S[i]
        S[i] = temp
        start += 1
        i -= 1
    
    return S

def maximum(S, i, j):
    if S[i] > S[j]:
        return i
    
    return j



def reverseSort(S):
    highestIndex = 0
    n = 0

    while n < len(S)-1:
        for i in range(1, len(S)-n):
            highestIndex = maximum(S, highestIndex , i)

        reverse(S, highestIndex)
        reverse(S, len(S)-n-1)
        n+=1
        highestIndex = 0

    return S

my_list=[4,2,5,1,3]
print(reverseSort(my_list))