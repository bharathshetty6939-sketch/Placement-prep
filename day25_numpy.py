import numpy as np
score=np.array([45, 88, 56, 92, 71])
print("minimum score is:",score.min())
print("Maximum score is:",score.max())
normalized_scores=(score - score.min()) / (score.max() - score.min())
print("NORMALIZED SCORE IS:",normalized_scores)
