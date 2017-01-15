import random
import sys
import pickle
	
sys.path.insert(0, '..')
import Euler

lim = int(sys.argv[1])

def inb(nb):
	"""
	exp = []
	xp = []
	d = Euler.factorization(nb)
	for key in d:
		xp.append(key)
		exp.append(d[key])
	"""

	xp = [2,3,5,7,11,13]
	#xp = itemlist = pickle.load(open("primeBelow120000","rb"))
	#print(xp)
	#print(exp)
	ln = len(xp)
	it = [0]*ln
	n = 1
	while 1:
	#for k in range(100):
		#n = 1
		#for e in range(ln):
		#	n *= xp[e]**it[e]

		for i in reversed(range(1,ln)):
			#n = 1
			#for e in range(ln):
			#	n *= xp[e]**it[e]
			if n > lim:
			#if it[i] == exp[i]:
				n //= xp[i]**it[i]
				it[i] = 0
				it[i-1] += 1
				n *= xp[i-1]
			else:
				break

		if n > lim:
			break

		#print(it[0],it[1],it[2])
		#print(it)
		
		############
		
		#print(k,"",end='')
		for i in range(ln):
			print(it[i],end='')
		print("",n)
		###########
		it[ln-1] += 1
		n *= xp[ln-1]


inb(60)

