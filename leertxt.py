#lectura de un archivo 
import ephem  as ep
#pasra sonlo un satlite 

def leertxt(nomdre):
	arch=open(nomdre)
	l1=arch.readline()
	while l1:
		l2=arch.readline()
		l3=arch.readline()
		sat=ep.readtle(l1,l2,l3)
		#print sat.name
		l1=arch.readline()
	arch.close()
	return sat
