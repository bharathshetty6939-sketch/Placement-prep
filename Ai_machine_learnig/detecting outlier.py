import numpy as np
data=np.array([170, 172, 168, 175, 120, 171])
mean=np.mean(data)
std1=np.std(data)
for x in data:
    if abs(x-mean)>(2*std1):
        print("Outlier is",x)