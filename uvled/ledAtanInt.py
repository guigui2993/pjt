from scipy.integrate import dblquad
import math
import numpy as np
from scipy.interpolate import interp1d

h = 1
relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975])#,0])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5])#,17.9])
ang *= math.pi/180

midAng = 18.2*math.pi/180
stiff = 500
t = math.pi/2-np.arctan(stiff*(ang-midAng))

pol_t = interp1d(np.concatenate((ang,np.array([0.35,0.33,0.38]))),np.concatenate((relInt/t,[0,0,0])), kind='cubic', bounds_error=False)

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
	return np.cos(theta)*pol_t(theta)*(math.pi/2-np.arctan(stiff*(theta-midAng)))

a = 1

#area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a/10, lambda x: 0, lambda x: a/10)
area = dblquad(lambda x, y: I_sqrt(a,x,y), 0, a, lambda x: 0, lambda x: a)
#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
#area = dblquad(lambda x, y: I_tst(a,x,y), 0, a, lambda x: 0, lambda x: a)
print(area)
