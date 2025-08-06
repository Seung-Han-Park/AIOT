import matplotlib.pyplot as plt
import numpy as np

number = np.random.normal(size=10000)
plt.hist(number, bins=50, density=True)
plt.title("Histogram of Normal Distributed Random Numbers")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()