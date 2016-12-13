from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d
"""
Try to find a polynomial that fit the best
The best is the linear ...
"""

theta = np.arange(-math.pi, math.pi, 0.2)
r = np.arange(0, 10, 0.25)

#relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975])
#ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5])
relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975,0,0])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5,17.9,90])

relInt2 = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975,0])
ang2 = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5,17.9])

#relIntTrick = np.array([0.05,0,0,0,0])
#angTrick = np.array([17.05,17.72,18,19,20])
#relIntTrick = np.array([0])
#angTrick = np.array([17.72])
#relIntTrick = np.array([0,0.001,0.0005,0.987,0.984])
#angTrick = np.array([17.72,17.7199,17.71985,1.545,1.6])

#relInt = np.append(relInt,relIntTrick)
#ang = np.append(ang,angTrick)

#a = np.arange(0, 16.4, 0.25)
a = np.arange(0, 20, 0.02)
pol = interp1d(ang2,relInt2, kind='cubic', fill_value=0, bounds_error=False)
pol2 = interp1d(ang,relInt, kind='slinear')
z1 = np.polyfit(ang, relInt, 1)
z2 = np.polyfit(ang, relInt, 5)
z3 = np.polyfit(ang, relInt, 3)
print(z1)
print(z2)
print(z3)
#plt.plot(ang,relInt,'x',a,pol(a),'r',a,np.polyval(z1,a),'g',a,np.polyval(z2,a),'b',a,np.polyval(z3,a),'-')
plt.plot(ang[0:-1],relInt[0:-1],'x',a,pol(a),'r',a,np.polyval(z2,a),'g',a,pol2(a),'b')
#plt.plot(ang,relInt,'x',a,np.polyval(z2,a),'g')

#T, R = np.meshgrid(theta,r)
#Z = pol(theta)


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
