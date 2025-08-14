import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3, 4, 5])
y = np.array([4, 6, 2, 3])

p = plt.figure(1)
plt.plot(x, y, color='YELLOW')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.grid()



q = plt.figure(2)
plt.scatter(0, 0, s=7000)
plt.xlim(-0.85, 0.85)
plt.ylim(-0.95, 0.85)
plt.show()