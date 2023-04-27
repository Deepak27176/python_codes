
def maxelements(input1):
    s = set(input1)
    count1 = 0
    max1 = 0
    k = ""
    for i in range(0,len(s)):
        count1 = input1.count(s[i])
        if count1>max1:
            k = s[i]
    return k
print(maxelements("abcdd"))