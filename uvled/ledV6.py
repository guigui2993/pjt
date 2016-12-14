from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d
"""
tanh with low stiff to approximate the fct with only a tanh
Just perfect :)
"""

relInt = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1,0.033])
#ang = np.array([16.4,14.75,13,11.6,10,8.65,7.1,5.8,4.3,2.5,0.0,19])
#ang *= math.pi/180
ang = np.array([ 0.286234  ,  0.25743606,  0.2268928 ,  0.20245819,  0.17453293, 0.15097098,  0.12391838,  0.1012291 ,  0.07504916,  0.04363323,0.,  0.33161256])


a_p=[-0.05,0.36]
y_p=[1.005,0.05]

#a_p=[]
#y_p=[]

relInt = np.append(relInt,np.array(y_p))
ang = np.append(ang,np.array(a_p))
#print(ang)
#pol = interp1d(ang,relInt, kind='slinear')
#pol = interp1d(ang,relInt, kind='cubic', fill_value=0, bounds_error=False)
pol = interp1d(ang,relInt, kind='cubic',bounds_error=False)

a = np.arange(min(ang), max(ang), 0.002)
#a *= math.pi/180

relIntExt = pol(a)

#t = np.tan(math.pi/2-relIntExt)

#zt = np.polyfit(a, t,5)
zp = np.polyfit(a, pol(a),5)

at = np.arange(-1, 85, 0.002)
at *= math.pi/180

"""
#pol_t = interp1d(np.concatenate((ang,np.array([0.35,0.33,0.38]))),np.concatenate((relInt/t,[0,0,0])), kind='cubic', bounds_error=False)
pol_t = interp1d(np.concatenate((ang,np.array([0.35,0.33,0.38]))),np.concatenate((relInt/t,[0,0,0])), kind='cubic', bounds_error=False)


z2 = np.polyfit(ang, relInt, 5)
print(z2)
#plt.plot(ang,relInt,'x',a,pol(a),'r',a,np.polyval(z1,a),'g',a,np.polyval(z2,a),'b',a,np.polyval(z3,a),'-')
#plt.plot(ang,relInt,'x',a,pol(a),'r',a,np.polyval(z2,a),'g',a,pol_t(a),'b',a,pol_t(a)*(math.pi/2-np.arctan(stiff*(a-midAng))),'k')
"""

plt.plot(ang,relInt,'x')
#plt.plot(a,t,'k')
plt.plot(at,np.polyval(zp,at)*(1+np.tanh((0.33-at)*20))/2,'r')
#plt.plot(a,np.polyval(zt,a),'r')
#plt.plot(a,math.pi/2-np.arctan(np.polyval(zt,a)),'g')

"""
plt.plot(a,pol(a),'r')
plt.plot(a,np.polyval(z2,a),'g')
plt.plot(a,(math.pi/2-np.arctan(stiff*(a-midAng)))/math.pi,'k')
plt.plot(a,np.polyval(z2,a)*(math.pi/2-np.arctan(stiff*(a-midAng)))/math.pi,'m')
"""
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
