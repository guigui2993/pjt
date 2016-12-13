from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from scipy.integrate import dblquad
import math
import numpy as np
from scipy.interpolate import interp1d

h = 1
relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975,0,0])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5,17.9,90])
ang *= math.pi/180
pol = interp1d(ang,relInt, kind='slinear')

def I_tst(a,x,y):
	return max(0,a-x-y)
	#return max(0,a)

def I_sqrt(a,X,Y):
	Z = I(np.arctan(np.sqrt(X**2+Y**2)))
	Z += I(np.arctan(np.sqrt((X-a)**2+Y**2)))
	Z += I(np.arctan(np.sqrt(X**2+(Y-a)**2)))
	Z += I(np.arctan(np.sqrt((X-a)**2+(Y-a)**2)))
	return Z

def I_tri(a,X,Y):
	Z = I(np.arctan(np.sqrt(X**2+Y**2)))
	Z += I(np.arctan(np.sqrt((X-a)**2+Y**2)))
	Z += I(np.arctan(np.sqrt((X-a/2)**2+(Y-math.sqrt(3)/2*a)**2)))
	return Z

def I(theta):
	#print(theta)
	#print("max: ", np.amax(theta))
	#print("min: ", np.amin(theta))
	#print(pol(theta))
	return np.cos(theta)*pol(theta)
	

a = 0.4
#area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a, lambda x: 0, lambda x: x)
area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
print(area)


fig = plt.figure()
ax = fig.gca(projection='3d')

xm,xM = -0.6, 1.2
ym,yM = -0.6, 1.2


X = np.arange(xm, xM, 0.03)
Y = np.arange(ym, yM, 0.03)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)

Z = I_tri(a,X,Y)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
