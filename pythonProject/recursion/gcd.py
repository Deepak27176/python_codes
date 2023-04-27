# a = int(input())
# b = int(input())


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


# print(gcd(a, b))
def longestPalindrome(s):
    j = len(s)
    max_str = ""
    while j > 0:
        for i in range(j):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > len(max_str):
                    max_str = s[i:j]
        j -= 1
    return max_str


print(longestPalindrome("malayalam"))
