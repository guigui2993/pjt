from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d

theta = np.arange(-math.pi, math.pi, 0.2)
r = np.arange(0, 10, 0.25)

relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,0])

a = np.arange(0, 16.4, 0.25)
pol = interp1d(ang,relInt, kind='cubic')
#plt.plot(ang,relInt,'x',a,pol(a),'r')

#T, R = np.meshgrid(theta,r)
Z = pol(theta)


"""
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

"""
plt.show()
#r = 
#x = 
