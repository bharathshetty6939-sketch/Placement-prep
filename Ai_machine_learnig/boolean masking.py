import numpy as np
data=np.array([22.5, 35.0, 18.2, 40.1, 12.5, 38.0]);
mask=data>30
filtered_data=data[mask]
print("Temp above 30degree is",filtered_data)