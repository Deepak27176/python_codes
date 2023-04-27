import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
twoDArr = np.array([[1,2,3,4],[5,6,7],[9,0,11,12,]])
#print(twoDArr[0][3])
# Traversing through ARRAY
for i in range(len(twoDArr)):
    for j in range(len(twoDArr[i])):
        print(twoDArr[i][j])