from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d
from scipy.integrate import dblquad

"""
tanh with low stiff to approximate the fct with only a tanh
Just perfect :)
The cos has nearly no effect
"""

relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1,0.033])
#ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0.0,19])
#ang *= math.pi/180
ang = np.array([ 0.286234  ,  0.25743606,  0.2268928 ,  0.20245819,  0.17453293, 0.15097098,  0.12391838,  0.1012291 ,  0.07504916,  0.04363323,0.,  0.33161256])


a_p=[-0.05,0.36]
y_p=[1.005,0.05]

relInt = np.append(relInt,np.array(y_p))
ang = np.append(ang,np.array(a_p))
pol = interp1d(ang,relInt, kind='cubic',bounds_error=False)

a = np.arange(min(ang), max(ang), 0.002)

relIntExt = pol(a)

zp = np.polyfit(a, pol(a),5)

at = np.arange(-1, 85, 0.002)
at *= math.pi/180

def pol(x):
	agx = 1
	s = 0
	for c in reversed(zp):
		s += c*agx
		agx *= x
	return s*(1+np.tanh((0.33-x)*20))/2



def I_tst(a,x,y):
	#return np.cos(np.arctan(np.sqrt(x**2+x**2)))
	return pol(np.arctan(np.sqrt(x**2+x**2)))
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
	return np.cos(theta)*pol(theta)

def maxf(x):
	t = np.arange(0, a, 0.002)
	y = I_sqrt(t)
	idx = y.index(max(y))
	
	ia = max(0,idx-2)
	ib = min(idx+2,len(y)-1)
	maxx = I_sqrt((ia+ib)/2)
	while True:
		if I_sqrt((3*ia+ib)/4) > maxx:
			maxx = I_sqrt((3*ia+ib)/4)
		elif I_sqrt((3*ib+ia)/4) > maxx:
			maxx = I_sqrt((3*ib+ia)/4)
		else:
			return maxx

a = 0.4

#plt.plot(at,I(at),'b')
#plt.plot(at,pol(at),'r')
#plt.plot(at,np.cos(at),'k')
#plt.plot(at,np.polyval(zp,at)*(1+np.tanh((0.33-at)*20))/2,'r')
#plt.plot(at,pol(at)*(1+np.tanh((0.33-at)*20))/2,'g')

#plt.show()

#area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a/10, lambda x: 0, lambda x: a/10)
area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a, lambda x: 0, lambda x: a)
sm = dblquad(lambda x, y: (I_sqrt(a,x,y)-area[0])**2, 0, a, lambda x: 0, lambda x: a)
#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
print(area)
print(sm)

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 1, 0.05)
Y = np.arange(0, 1, 0.05)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
Z = I_sqrt(a,X,Y)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.show()
