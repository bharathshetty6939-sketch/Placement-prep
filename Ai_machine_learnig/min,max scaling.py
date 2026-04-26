import numpy as np
data=np.array([10,100,0,100000])
d_min=np.min(data)
d_max=np.max(data)
newdata=data-d_min/d_max-d_min
print("Original data",data)
print("scaled data (0 to 1)",newdata)