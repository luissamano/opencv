"""
# Abrir el entorno de Anaconda
"C:\ProgramData\Anaconda3\Scripts\activate.bat"

# Verificar las versiones de Python y pip
python -V
pip -V

# Instalar pip
python -m pip install -U pip

# Actualizar pip
python -m pip --upgrade -U pip

# URL para descargar WHL de OpenCV
http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

# Instalar el archivo pip
pip install "opencv_python-3.4.4+contrib-cp37-cp37m-win32.whl"
"""




import cv2
 
# Cargamos la imagen del disco duro
imagen = cv2.imread("images\logo.jpg")
 
cv2.imshow("prueba", imagen)
cv2.waitKey(0)