s = "adam"
max_len = 0
m_pal  = ""
for i  in range(len(s)):
    l=r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1 > max_len:
            m_pal = s[l:r+1]
            max_len = r-l+1

        l -= 1
        r+=1
    l =i
    r = i+1

    while l>0 and r<len(s) and s[l]==s[r]:
        if r-l+1 > max_len:
            m_pal = s[l:r+1]
            max_len = r-l+1
        l -= 1
        r+=1


print(m_pal)
