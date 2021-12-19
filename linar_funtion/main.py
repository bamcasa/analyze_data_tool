import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import math

points = [(1,2),(2,5),(0,0),(4,3)]


P_x = []
for i in range(len(points)):
    P_x.append(points[i][0])
P_x = np.array(P_x)
s = P_x.argsort()
print(P_x)
print(s)

P_x = np.array(sorted(list(P_x)))
print(P_x)
sorted_points = []
for i in range(len(s)):
    sorted_points.append(points[s[i]])

points = sorted_points

print(sorted_points)

m = []
n = []

for i in range(len(P_x) - 1):
    x1,y1 = points[i]
    x2,y2 = points[i+1]
    m.append((y2 - y1)/(x2 - x1))          # 기울기 m 계산
    n.append(y1 - (m[i] * x1))
print(m,n)
x = []
for i in range(len(P_x)-1):
    x.append(np.linspace(P_x[i],P_x[i+1], 1000))
y = []
for i in range(len(m)):
    y.append(m[i] * x[i] + n[i])

#plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 5


fig, ax = plt.subplots()
#ax1.spines['left'].set_position('center')
#ax1.spines['bottom'].set_position('center')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params('both', length=0)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

#plt.xlim([0, 5])
#plt.ylim([0, 20])
plt.axis('auto')
for i in range(len(P_x) - 1):
    plt.plot(x[i], y[i])

tm = time.localtime(time.time())

plt.show()

