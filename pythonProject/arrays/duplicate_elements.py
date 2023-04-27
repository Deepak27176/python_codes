string = input()
c = 0

for i in string:
    if string.count(i)==1:
        c +=1
    if c==2:
        print(i)
        break
if c!=2:
    print("Inavlid String")
