import warnings
import numpy as np
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
twoDArr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12]])
print(twoDArr)
twoDArr = np.delete(twoDArr, 2, axis=0)
print(twoDArr)
