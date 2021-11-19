import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import math

x_range = [-10,10]

x = np.linspace(x_range[0], x_range[1], 1000)
y = x**3 - x**2 + x + 10

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

plt.plot(x, y)

tm = time.localtime(time.time())
plt.savefig(f'graph_image/{tm.tm_mon}M{tm.tm_mday}D{tm.tm_hour}H{tm.tm_min}m{tm.tm_sec}s.png', dpi=200)

plt.show()

