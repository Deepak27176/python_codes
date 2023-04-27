Dict = {
    "a": ["c"],
    "b": ["c", "d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["h", "f"],
    "f": ["g"]
}


def fun(dic, c, lis):
    if c in dic:
        for i in dic[c]:
            if i not in lis:
                lis = fun(dic, i, lis)
        lis.append(c)

    else:
        lis.append(c)
    return lis


res = []
for key, value in Dict.items():
    if key not in res:
        res = (fun(dic=Dict, c=key, lis=res))
print(res[::-1])
