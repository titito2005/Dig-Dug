# Dig-Dug-Remastered - MARDA


### Instrucciones de ejecución:

**Nota:** prueba.py es un ejemplo de como se puede implementar un juego usando el MARDA. Estas instrucciones se van a enfocar en poder ejecutar prueba.py.

##### Método 1: Usando Visual Studio:
Es el método más rápido si ya tiene cualquier versión de Visual Studio con el módulo de desarrollo de Python instalado.
- Abrir el proyecto con Visual Studio
- Buscar y expandir la lista de ambientes virtuales de Python, en la ventana del explorador de la solución.
- Hacer click derecho en el ambiente virtual que aparezca (Llamado Python 3.7 o similar)
- Estripar en la opción de instalar dependencias a partir de requirements.txt
- Ejecutar con f5

##### Método 2: Creando y activando [ambientes virtuales:](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
Requiere python3 con los modulos de pip y venv instalados
###### Windows:
- Abrir cmd.exe y navegar hasta el directorio raiz del proyecto (donde se encuentra Digdug.py)
- Crear el ambiente virtual con `py -m venv env`
- Activar el ambiente virtual con `.\env\Scripts\activate`
- Instalar pygame con `pip install pygame --pre`
- Ejecutar el programa con `py prueba.py`
###### Linux:
- Abrir el terminal y navegar hasta el directorio raiz del proyecto (donde se encuentra Digdug.py)
- Crear el ambiente virtual con `python3 -m venv env`
- Activar el ambiente virtual con `source env/bin/activate`
- Instalar pygame con `pip install pygame --pre`
- Ejecutar el programa con `python3 prueba.py`
