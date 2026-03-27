import numpy as np
data=np.array([170, 180, 165, 175, 182])
standardization=(data-data.mean())/(data.std())
print("The standardization is",standardization)