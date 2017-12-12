import os
import os.path
root_ob = 'htm'

lis=[]
grafic=[]
raiz=os.getcwd()
print raiz
os.chdir(root_ob)
print os.getcwd()
#tomando las direccines de cada uno de la ciudades.  
#for fileList in os.walk(root_ob):
	#fileList=str(fileList)
#print fileList

#manejo de archivos 
#toma los Datos ya exixtentes 
#fi=os.path("Sat_see","Datos_obs")

##cargando el archivo ruta de las carpeta 
#with open(fi+".pickle", "rb") as input_file:
	#D_obs=cPickle.load(input_file)

#convirtiendo los datos de una lista de str.

#datos=fileList.split("[]")[1]
#print datos
#for l in datos.split("'"):
	#if (".html" in l):
		#grafic.append(l)

#print grafic
s=os.path.abspath("az_alt_gra.html")
print s
print os.path.exists(s)

os.chdir(raiz)
print os.getcwd()
