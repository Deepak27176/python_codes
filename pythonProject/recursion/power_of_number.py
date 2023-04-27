n = int(input())
exp = int(input())


def power_of_num(n, exp):
    assert exp >= 0, 'exponent must be positive integer'
    if exp == 0:
        return 1
    else:
        return n * power_of_num(n, exp - 1)


print(power_of_num(n=n, exp=exp))
