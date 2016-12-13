from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d
"""
Approximate the fct with 1/cosh
"""

relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.033])
ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0.0,19])

#relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,0.975])#,0])
#ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0,1.5])#,17.9])

ang *= math.pi/180
#pol = interp1d(ang,relInt, kind='slinear')
#pol = interp1d(ang,relInt, kind='cubic', fill_value=0, bounds_error=False)
pol = interp1d(ang,relInt, kind='cubic',bounds_error=False,fill_value=0)

stiff = 20
#midAng = 10*math.pi/180
#t = (math.pi/2-np.arctan(stiff*(ang-midAng)))/math.pi



a1 = np.arange(0, 85*math.pi/180, 0.0002)
c = np.cosh(stiff*a1)
relInt1 = pol(a1)
#pol_t = interp1d(np.concatenate((ang,np.array([0.35,0.33,0.38]))),np.concatenate((relInt/t,[0,0,0])), kind='cubic', bounds_error=False)
#pol_t = interp1d(np.concatenate((ang,np.array([0.35,0.33,0.38]))),np.concatenate((relInt/t,[0,0,0])), kind='cubic', bounds_error=False)
#zt = np.polyfit(ang, relInt/t,5)
zc = np.polyfit(a1, relInt1*c,5)
#zc_bp = interp1d(a1,relInt1*c, kind='cubic')

a = np.arange(0, 20, 0.002)
a *= math.pi/180

z2 = np.polyfit(ang, relInt, 5)
print(z2)
#plt.plot(ang,relInt,'x',a,pol(a),'r',a,np.polyval(z1,a),'g',a,np.polyval(z2,a),'b',a,np.polyval(z3,a),'-')
#plt.plot(ang,relInt,'x',a,pol(a),'r',a,np.polyval(z2,a),'g',a,pol_t(a),'b',a,pol_t(a)*(math.pi/2-np.arctan(stiff*(a-midAng))),'k')
plt.plot(ang,relInt,'x')
plt.plot(a1,pol(a1),'r')
plt.plot(a,np.polyval(z2,a),'g')
#plt.plot(a1,1/c,'k')
#plt.plot(a,zc_bp(a)/np.cosh(stiff*a),'k')
plt.plot(a,np.polyval(zc,a)/np.cosh(stiff*a),'k')
print("a",a)
print("c",relInt1/c)
print(np.polyval(zc,a))
print(np.polyval(zc,a)/np.cosh(stiff*a))
#print(zc_bp(a)/np.cosh(stiff*a))
#plt.plot(a,(math.pi/2-np.arctan(stiff*(a-midAng)))/math.pi,'k')
#plt.plot(a,np.polyval(z2,a)*(math.pi/2-np.arctan(stiff*(a-midAng)))/math.pi,'m')

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
