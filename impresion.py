
### librerias para el manejo de los archivos 
import cPickle
import pickle
from os import path
import yaml
import os
import os.path

sav_sat=path.join("Sat_see","satelites.pickle")
with open(sav_sat, "rb") as input_file:
	sat_v=cPickle.load(input_file)

sat_l=list(sat_v.keys())


#root_ob = 'htm'

#os.chdir(root_ob)

#fil_rut=os.path.abspath(tipo)
#os.chdir(raiz1)
c=0
for nom in sat_l:
	gra_dic=yaml.load(open(path.join("Sat_datos",nom)))
	
	x=gra_dic["Escal_time"]
	al=gra_dic["ant_alt"]
	az=gra_dic["ant_az"]
	lon=gra_dic["longitud"]
	lati=gra_dic["latitud"]
	t=gra_dic["Tiempo"]
	fiche=nom+".txt"
	arch=open(fiche,'w')
	for n in range(0,len(x)):
		
		s=("%s\t %s\t %s " % (str(t[n]),str(float("{0:.4f}".format(az[n]))),str(float("{0:.4f}".format(al[n]))))) 
		print s
		arch.write(s)
		arch.write('\n')
		
	arch.close()
