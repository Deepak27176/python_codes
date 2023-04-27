s = input()

def reverse(string):
    string1 =""
    if len(string) == 1:
        return string
    else:
        string1 = string[len(string)-1:len(string)]+reverse(string[:-1])
    print(string1)



reverse(s)
