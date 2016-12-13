from scipy.integrate import dblquad
import math
import numpy as np
from scipy.interpolate import interp1d

h = 1
relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975,0,0])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5,17.9,90])
relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975,0])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5,17.9])
ang *= math.pi/180
#pol = interp1d(ang,relInt, kind='slinear')
pol = interp1d(ang,relInt, kind='cubic', fill_value=0, bounds_error=False)

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

a = 1

#area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a/10, lambda x: 0, lambda x: a/10)
area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a, lambda x: 0, lambda x: a)
#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
print(area)
