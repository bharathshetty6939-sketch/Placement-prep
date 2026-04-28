import numpy as np
study_hours = [2, 5, 8, 10]
marks = [40, 55, 80, 95]
matrix=np.corrcoef(study_hours,marks)
print(matrix[0,1])