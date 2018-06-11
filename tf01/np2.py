import numpy as np
import matplotlib.pyplot as plt
#梯度下降

a = range(-100, 101)
print(a)
b = np.power(a, 2)
print(b)
c = np.multiply(a,2)
T = np.arctan2(b,a) # for color value

plt.figure()

plt.scatter(a, b, s=75, c=T, alpha=.5)


for x, y in zip(a, b):
    plt.text(x, y, '%.2f' % y, ha='center', va='top')

plt.plot(a, b, color='blue', linewidth=1.0, linestyle='-')

plt.xlim((-100, 100))
plt.ylim((-100, 100))

ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_position(('data', 0))
ax.spines['top'].set_position(('data', 0))
plt.show()