# TIS(Tracking interface for satellites)
El proyecto TIS es un programa desarrollado en Python para rastreo satelital en tiempo real, 
permite seguir múltiples rutas desde una ubicación predeterminada, muestra el tiempo de línea de vista del satélite,
estima los ángulos de orientación de la antena y cuenta con un módulo de comunicación con una antena
a través de USB o red. 

# Instalación

El programa requiere las siguientes librerías:

### Librería  PyEphem:
```
$ sudo pip2 install pyephem
```

### Librería pyQt:
```
$ sudo apt install python-qt4
$ sudo apt install pyqt4-dev-tools
$ sudo apt install libqt4-designer
``` 

### Librería Bokeh:
```
$ sudo pip2 install bokeh
$ sudo pip2 install --pre -i https://pypi.anaconda.org/bokeh/channel/dev/simple bokeh --extra-index-url https://  pypi.python.org/simple/
```

### Librería folium:
```
$ sudo pip2 install folium
```
### Librería Basemap:
```
$ sudo apt install python-matplotlib
$ sudo apt install python-mpltoolkits.basemap
```
### Librería requests
```
$ sudo pips install requests
```

### Librería Hamlib:
```
$ sudo apt install hamlib-dev libasound-dev libv41-dev
$ sudo apt install libhamlib-utils
```
### Librería BeautifulSoup:
```
$ sudo pip2 install beautifulsoup4
```

### Librería ntplib:
```
$ sudo pip2 install ntplib
```

### Librería pygeocoder:
```
$ sudo pip2 install pygeocoder
```

### Librería python-tk:
```
$ sudo apt install python-tk 
```

# El programa principal del proyecto es TIS.py
```
$ python TIS.py
```

## Para el control de la antena se utiliza la librería Hamlib.

### Conectar la antena por USB: 
1. Para habilitar los permisos en el puerto USB
```
$ sudo chmod 777 /dev/ttyACM0
```
2. En el menú de Archivo se selecciona Antena y luego PC.

### Conectar la antena por red:
1. La antena debe tener habilitado el servidor de Hamlib
2. En el archivo rot_w_call_red.py se la IP y el puerto.
3. En el menú de Archivo se selecciona Antena y luego Red.
