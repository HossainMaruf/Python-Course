import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(-1000, 1000)])
y = x**2

plt.plot(x, y)
plt.xlim(-10, 10)
plt.ylim(-100, 100)
plt.grid()
plt.show()
