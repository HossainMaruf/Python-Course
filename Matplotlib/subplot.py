import numpy as np
import matplotlib.pyplot as plt

x = np.array([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])

plt.subplot(3, 2, 1)
plt.plot(x, x**2, color="RED", linestyle="dashed", label="f(x) = x^2")
plt.xlabel('values of x')
plt.ylabel('values of y')
plt.title('Graph Plotting')
plt.grid()
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(x, x**3, color="PURPLE", linestyle="dotted", label="f(x) = x^3")
plt.xlabel('values of x')
plt.ylabel('values of y')
plt.title('Graph Plotting')
plt.grid()
plt.legend()


plt.subplot(3, 2, 5)
plt.plot(x, x**4, color="PURPLE", linestyle="dotted", label="f(x) = x^4")
plt.xlabel('values of x')
plt.ylabel('values of y')
plt.title('Graph Plotting')
plt.grid()
plt.legend()


plt.subplot(3, 2, 6)
plt.plot(x, x**5, color="PURPLE", linestyle="dotted", label="f(x) = x^5")
plt.xlabel('values of x')
plt.ylabel('values of y')
plt.title('Graph Plotting')
plt.grid()
plt.legend()

plt.show()