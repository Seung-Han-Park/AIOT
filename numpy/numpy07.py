import numpy as np
import time

np.random.seed(int(time.time()))
randomNumbers = np.random.randint(1, 100, size=10)
print("Random Numbers:", randomNumbers)
randomNumbersTwoDim = np.random.randint(1, 100, size=(3, 4))
print("2D Random Numbers:\n", randomNumbersTwoDim)
randomNumbersTwoDim = np.random.randint(1, 100, size=(2, 3, 4))
print("3D Random Numbers:\n", randomNumbersTwoDim)
randomNumbersTwoDim = np.random.normal(loc=0, scale=1, size=10)