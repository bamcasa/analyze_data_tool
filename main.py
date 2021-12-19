from fractions import Fraction
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import math
import copy


def function(x, a, *args):
    n = len(args)
    #print(f"{n}차 함수")

    coefficients = list(args)
    coefficients.insert(0, a)

    #print(coefficients)
    x1 = np.array(x).astype(np.float64)
    solution = x1 * 0

    for i in range(n, -1, -1):
        solution += coefficients[n-i] * x ** i

    return solution

def solver(equls):

    #print(equls)

    n = len(equls[0]) - 1
    print(f"{n}원 연립 일차 방정식")

    matA = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matA[i][j] = equls[i][j]

    matj = copy.deepcopy(matA)

    detA = np.linalg.det(matA)

    result  = []

    for j in range(n):
        for i in range(n):
            matj[i][j] = equls[i][-1]
        detj = np.linalg.det(matj)
        result.append(detj/detA)

        matj = copy.deepcopy(matA)

    return result


point = [(10,50), (2,10), (9,7)] #접접의 좌표

P_x = []
for i in range(len(point)):
    P_x.append(point[i][0])
P_x = sorted(P_x)
P_x = np.array(P_x)

a = 1 #최고차항의 계수

P_count = len(P_x)

X = np.arange(P_count)
Y = np.arange(P_count)

for i in range(P_count):
    X[i], Y[i] = point[i]

#print("==============")
#print(X,Y)

equations = []

for i in range(P_count):
    n = P_count
    temp = []
    for j in range(n):
        value = X[i] ** (n-1-j)
        temp.append(value)
    temp.append(Y[i] - a * X[i] ** n)
    equations.append(temp)
print(equations)

temp = solver(equations)

coes = []
coes.append(a)
for i in temp:
    coes.append(i)

print(coes)


#for i in range(len(point)):
#    print(point[i][1], function(point[i][0],a,b,c,d),abs(point[i][1] - function(point[i][0],a,b,c,d)))



#solutions = [(-2*b + ((2*b)**2 - 4*3*a*c)**(1/2))/(2*3*a),(-2*b - ((2*b)**2 - 4*3*a*c)**(1/2))/(2*3*a)]
#solutions = sorted(solutions)

#M = solutions[1] - solutions[0]

#x_range = [int(solutions[0] - M) - 10, int(solutions[1] + M) + 10]
x_range = [P_x[0],P_x[-1]]
#print(x_range)

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
#print(P_x,function(P_x,a,b,c,d))
ax1.set_zorder(ax2.get_zorder() - 10)
#ax1.patch.set_visible(False)



#plt.xlim([P_x[0], P_x[-1]])
#plt.ylim(int(function(P_x[0] - 1.5,a,b,c,d)), int(function(P_x[-1],a,b,c,d)))


#plt.axis('scaled')


tm = time.localtime(time.time())
plt.savefig(f'graph_image/{tm.tm_mon}M{tm.tm_mday}D{tm.tm_hour}H{tm.tm_min}m{tm.tm_sec}s.png', dpi=200)

plt.show()

