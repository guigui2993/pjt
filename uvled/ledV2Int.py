from scipy.integrate import dblquad
import math
import numpy as np
from scipy.interpolate import interp1d

h = 1
relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.033])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0.0,19])

ang *= math.pi/180
#pol = interp1d(ang,relInt, kind='slinear')

midAng = 18.5*math.pi/180
stiff = 500
t = math.pi/2-np.arctan(stiff*(ang-midAng))

zt = np.polyfit(ang, relInt/t,5)

def pol(a):
	return np.polyval(zt,a)*(math.pi/2-np.arctan(stiff*(a-midAng)))

def I_tst(a,x,y):
	#return np.cos(np.arctan(np.sqrt(x**2+x**2)))
	return pol(x)
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


for a in np.array(list(range(10)))/10:
	#a = 1

	print(pol(a))
	#area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a/10, lambda x: 0, lambda x: a/10)
	#area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a, lambda x: 0, lambda x: a)
	#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
	area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
	print(a,area)
