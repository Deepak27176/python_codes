

# def InvertWordsInSameOrder(str):
#     res=""
#     str = str.split(sep=" ")
#     for word in str:
#         res += word[::-1]+" "
#     return res
#
# print(InvertWordsInSameOrder("Hello wOrld"))
def decrypt(str):
    res = ""
    str=list(str)
    for ch in str:
        if ord(ch) <= 109:
            k = ord(ch)+(ord(ch)-97)
            k = 122-k
            k = ord(ch)+k
            res += chr(k)
        else:
            k = ord(ch)+(ord(ch)-97)-122
            k = ord(ch)-k
            res+= chr(k)
    return res
print(decrypt("vmxibkgrlm"))
