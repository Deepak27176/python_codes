n = int(input())


def dec_to_bin(m):
    assert m >= 0, 'number should be positive'
    if m//2 == 0:
        return 1
    else:
        return m % 2 + 10*dec_to_bin(m//2)


print(dec_to_bin(n))
