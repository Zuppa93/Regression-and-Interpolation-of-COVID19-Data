import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from scipy import interpolate

x = np.arange(0,5)
y = [1,2,1,4,3]


mpl.style.use('seaborn')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,'o')

plt.savefig('Scatterset.png',dpi=300,bbox_inches='tight')

plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

f = interpolate.interp1d(x,y)
mod = f(x)
ax.plot(x,mod,x,y,'o')

plt.savefig('LinearSpline.png',dpi=300,bbox_inches='tight')

plt.show()