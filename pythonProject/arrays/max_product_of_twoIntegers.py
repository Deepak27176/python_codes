import numpy as np

myarray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14,
                    35, 16, 27, 58, 19, 21])
max_pro = 0
for i in range(len(myarray)):
    for j in range(i+1, len(myarray)):
        if myarray[i]*myarray[j] > max_pro:
            max_pro = myarray[i]*myarray[j]
            pairs = str(myarray[i])+" "+str(myarray[j])
print(max_pro)
print(pairs)