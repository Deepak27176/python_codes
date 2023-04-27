import numpy as np
twoDArr = np.array([[1,2,3,4],[5,6,7,8],[9,0,11,12,]])
print(twoDArr)
twoDArr=np.insert(twoDArr,0,[[13,14,15,16]],axis=0)
print(twoDArr) # if axis = 0 adds row
twoDArr=np.insert(twoDArr,0,[[13,14,15,16]],axis=1)
print(twoDArr)  # if axis = 1 adds column