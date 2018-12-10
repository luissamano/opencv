# opencv 
## Inteligencia Artificial II

Los componentes necesarios para el proyecto son 

1. python >= 3.7
1. pip >= 18.1
1. opencv 

Se recomienda utlizar Anaconda para la prueba de este repositorio. abrimos una consola para correr el siguiente comando y asi activar el enetorno de anaconda.
```
activate base
```

Instalar pip primero hay que descargar el archivo [get-pip.py](https://bootstrap.pypa.io/get-pip.py) lo guadamos dentro de nuestro disco duro, despues nos direcionamos a la carpeta donde lo guardamos y nos disponemos a correr los siguientes comandos
```
python get-pip.py
pip -V
```


Actualizar pip, para mayor informacion puedes consultar la pagina oficial [pip.pypa.io](https://pip.pypa.io/en/stable/installing/).
```
python -m pip install -U pip
```


URL para descargar WHL de OpenCV, debemos buscar la version que sea compatible con nuestro entorno
```
http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
```

Instalar el archivo pip, en mi caso (x64 y Python 3.7), deberas cambiar el nombre depediendo de la arquitectura de tu pc.
```
pip install "opencv_python-3.4.4+contrib-cp37-cp37m-win_amd64.whl"
```

Para correr cualquier script, hay que dirigirnos dentro de la carpeta donde se extrajeron los archivos con la instrucion cd.
```
cd ~\opencv\opencv_basic
python basic.py
```

 > @SamanoCedillo 