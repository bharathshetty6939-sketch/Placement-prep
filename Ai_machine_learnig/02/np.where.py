import numpy as np
data=np.array([45, 88, 56, 92, 71, 33])
data1=np.where(data<40)
print("Index where score less then 40 are",data1[0])