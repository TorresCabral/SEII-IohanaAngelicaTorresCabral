import numpy as np
import matplotlib.pyplot as plt

a1 = 2*np.random.randn(10000) + 10

np.mean(a1)
np.std(a1)
np.percentile(a1, 80)

x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y, x) 
y_int = np.cumsum(y) * (x[1]-x[0])

np.cumsum(np.array([1,2,3,4]))

plt.plot(x, y)
plt.plot(x, dydx)
plt.plot(x, y_int)
