
# with open("C:/Users/IND/Desktop/my_file.txt", mode="r") as file:
#     print(file.read())
big_list1 = [[1,2 ,3],[6,7],[8,9]]

big_list2 = [[1,2 ,3],[6,7],[8,9]]

for  i in range(0,len(big_list1)):
    big_list1[i].extend(big_list2[i])
print(big_list1)