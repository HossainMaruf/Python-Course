import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 0, 3])
y = np.array([1, 2, -3])
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.grid()

x = np.array([1, -2, 6])
y = np.array([5, 1, 2])
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.grid()

plt.show()