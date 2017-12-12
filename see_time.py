#funcio para otener una tabla con los valors necesars para que se arele vante 
import datetime as dat

def see_time(hora_ini,hora_fin):
	
	li=[datetime.strptime(("00:00"),"%M:%S")]
	ti_see=ti_final-ti_ini
	midnight = ti_ini
	dt=[ti_ini]
	indice=1
	
	if ti_see>dat.timedelta(days=31):
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(hours=5)
			dt.insert(indice,midnight)
			indice=indice+1
		return dt

	elif ti_see>dat.timedelta(days=1):
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(hours=1)+dat.timedelta(minutes=0)
			dt.insert(indice,midnight)
			indice=indice+1
		return dt

	elif ti_see>dat.timedelta(hours=1):
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(minutes=1)+dat.timedelta(seconds=30)
			dt.insert(indice,midnight)
			indice=indice+1
		return dt

	elif ti_see>dat.timedelta(minutes=1):
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(minutes=0)+dat.timedelta(seconds=30)
			dt.insert(indice,midnight)
			indice=indice+1
		return dt

#Timepo de vista 


