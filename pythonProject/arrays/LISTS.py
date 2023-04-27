lis = []
count1 = 0
n = int(input("Enter number of days:"))
for i in range(0,n):
    k = int(input(f"enter day{i+1} high temperature:"))
    lis.append(k)
avg = sum(lis)/len(lis)
print(f"Average:{avg}")
for i in lis:
    if i>avg:
        count1 += 1
print(f"{count1} days above avg temp")

