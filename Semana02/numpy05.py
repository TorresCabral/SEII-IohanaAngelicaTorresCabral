import numpy as np
import matplotlib.pyplot as plt

N = 10000
x = np.linspace(0,10,N+1)
y = np.exp(-x/10)*np.sin(x)
plt.plot(x,y)

#-------------------------------------

np.mean(y[(x>=4)*(x<=7)])
np.std(y[(x>=4)*(x<=7)])

#-------------------------------------

np.percentile(y[(x>=4)*(x<=7)], 80)

#-------------------------------------

plt.plot(x, np.gradient(y,x))

#-------------------------------------

dydx = np.gradient(y,x)
x[:1][dydx[1:] * dydx[:-1] < 0]

#-------------------------------------
#-------------------------------------

nums = np.arange(0, 1000, 1)
sum(nums[(nums%4 != 0) * (nums%7 != 0)])

#-------------------------------------
#-------------------------------------

theta = np.linspace(0, 2*np.pi, 1000)
r = 1 + 3/4 * np.sin(3*theta)
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x,y)

#-------------------------------------

A = 1/2 * sum(r**2) * (theta[1]-theta[0])
sum(np.sqrt(r**2 + np.gradient(r, theta)**2)) * (theta[1]-theta[0])

#-------------------------------------
#-------------------------------------

kt = np.linspace(0, 3, 100)
P = (1/(1+np.exp(-kt))) ** 4
E = np.cumsum(P) * (kt[1] - kt[0])
plt.plot(kt, P)
plt.plot(kt, E)
