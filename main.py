from fractions import Fraction
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import math

def function(x,a,b,c,d):
    solution = (a * x ** 3) + (b * x ** 2) + (c * x) + d
    return solution

def solver(first, second, third):
    a1, b1, c1, d1 = first[0:4]
    a2, b2, c2, d2 = second[0:4]
    a3, b3, c3, d3 = third[0:4]

    delta = ((a1*b2*c3 + a3*b1*c2 + a2*b3*c1) - (a3*b2*c1 + a2*b1*c3 + a1*b3*c2))

    x = ((b2*c3*d1 + b1*c2*d3 + b3*c1*d2) - (b2*c1*d3 + b1*c3*d2 + b3*c2*d1)) / delta

    y = ((a1*c3*d2 + a3*c2*d1 + a2*c1*d3) - (a3*c1*d2 + a2*c3*d1 + a1*c2*d3)) / delta

    z = ((a1*b2*d3 + a3*b1*d2 + a2*b3*d1) - (a3*b2*d1 + a2*b1*d3 + a1*b3*d2)) / delta

    return [x, y, z]

point = [(5,2), (1,0), (9,7)] #접접의 좌표


P_x = []
for i in range(len(point)):
    P_x.append(point[i][0])
P_x = sorted(P_x)
P_x = np.array(P_x)

a = 1

x1, y1 = point[0]
equation_1 = [x1**2, x1, 1, y1 - a * x1**3]
x2, y2 = point[1]
equation_2 = [x2**2, x2, 1, y2 - a * x2**3]
x3, y3 = point[2]
equation_3 = [x3**2, x3, 1, y3 - a * x3**3]
print(equation_1,equation_2,equation_3)

temp = solver(equation_1,equation_2,equation_3)
b,c,d = temp
print(a,b,c,d)


for i in range(len(point)):
    print(point[i][1], function(point[i][0],a,b,c,d),abs(point[i][1] - function(point[i][0],a,b,c,d)))



#solutions = [(-2*b + ((2*b)**2 - 4*3*a*c)**(1/2))/(2*3*a),(-2*b - ((2*b)**2 - 4*3*a*c)**(1/2))/(2*3*a)]
#solutions = sorted(solutions)

#M = solutions[1] - solutions[0]

#x_range = [int(solutions[0] - M) - 10, int(solutions[1] + M) + 10]
x_range = [P_x[0],P_x[-1]]
print(x_range)

x = np.linspace(x_range[0], x_range[1], 1000)
#x = np.linspace(P_x[0], P_x[-1], 1000)
y = function(x,a,b,c,d)

plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 5

#plt.xticks([1,2,3])
#plt.yticks([1,2,3])



fig, ax1 = plt.subplots()
#ax1.spines['left'].set_position('center')
#ax1.spines['bottom'].set_position('center')
ax1.spines['left'].set_position(('data', 0))
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.tick_params('both', length=5)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

ax1.plot(x, y)

ax2 = ax1#.twinx()
ax2.set_xlim(ax1.get_xlim())
ax2.set_ylim(ax1.get_ylim())
ax2.spines['right'].set_position(('data', 0))
ax2.scatter(P_x, function(P_x,a,b,c,d), s=50, c='r')
print(P_x,function(P_x,a,b,c,d))
ax1.set_zorder(ax2.get_zorder() - 10)
#ax1.patch.set_visible(False)



#plt.xlim([P_x[0], P_x[-1]])
#plt.ylim(int(function(P_x[0] - 1.5,a,b,c,d)), int(function(P_x[-1],a,b,c,d)))


#plt.axis('scaled')


tm = time.localtime(time.time())
plt.savefig(f'graph_image/{tm.tm_mon}M{tm.tm_mday}D{tm.tm_hour}H{tm.tm_min}m{tm.tm_sec}s.png', dpi=200)

plt.show()
