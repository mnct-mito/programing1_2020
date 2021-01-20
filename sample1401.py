# 最小二乗法 y=ax で近似
import numpy as np
import matplotlib.pyplot as plt
def reg1dim1(x, y):
    a = np.dot(x, y) / (x**2).sum()
    return a
x = np.array([0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
y = np.array([6.5,13.0,19.7,26.4,33.5,39.8,46.2,53.0,59.9,66.5])
a = reg1dim1(x, y)
print(a)
plt.scatter(x, y, color="k")
xmax = x.max()
plt.plot([0,xmax],[0,a*xmax],color="r")
plt.show()

# 最小二乗法 y=ax+b で近似
import numpy as np
import matplotlib.pyplot as plt
def reg1dim2(x, y):
    n = len(x)
    a = ((np.dot(x, y) - y.sum() * x.sum() / n) / ((x**2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum()) / n
    return a, b
x = np.array([0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
y = np.array([6.5,13.0,19.7,26.4,33.5,39.8,46.2,53.0,59.9,66.5])
a, b = reg1dim2(x, y)
print(a)
print(b)
plt.scatter(x, y, color="k")
xmax = x.max()
plt.plot([0, xmax], [b, a * xmax + b], color = "r")
plt.show()