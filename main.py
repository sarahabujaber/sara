import numpy as np
x = np.array([[1,2,3,4,5],[4,5,6,12,4],[1,23,45,4,7]])

#(3,5)
y = np.array([[1,2,3,4,5],[4,5,6,12,4],[1,23,45,4,7],[1,3,4,5,6],[1,3,2,5,3]])

print(x)
print(x.shape)
print(x.reshape(15))
print(np.where(x == 4))
print(x.T)
print(x.T.shape)


