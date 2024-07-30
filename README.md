# Proyectos con Python

## Entornos virtuales

Los entornos virtuales sirvern para mantener aislados un entorno de trabajo en cada proyecto, con la intención de mantener versiones especificas de las librerías instaladas, para que cuando se utilice este proyecto no entre en conflicto con otro proyecto que utilice otras versiones de las librerías instaladas

Primero hay que instalar la siguiente librería

```bash
pip install pipenv
```

Una vez que contamos con la librería anterior, para crear un nuevo entorno de trabajo, dentro de la carpeta del proyecto que vamos a trabajar, instalar la primer librería utilizada ahora intercambiadon el instalador de **Python** `pip` por `pipenv`

```bash
pipenv install django
```

Para desinstalar una dependencia dentro del entorno de trabajo, ejecutar el siguiente comando:

```bash
pipenv uninstall django
```

Si queremos instalar una versión en especifico de la librería en nuestro proyecto, ejecutar el siguiente comando:

```bash
pipenv install requests==2.10.*
```

Para mostrar todos los paquetes que pueden ser actualizados a una última versión, ejecutar el siguiente comando:

```bash
pipenv update --outdated
```

Si quiero actualizar las librerías a las versiones recientes, ejecutar el siguiente comando:

```bash
pipenv update
```

Para ver la ruta donde creo la carpeta del entorno virtual, ejecutar el siguiente comando:

```bash
pipenv --venv
```

Para activar el entorno virtual, hay que entrar dentro de la carpeta del proyecto donde se creo el entorno virtural y ejecutar el siguiente comando:

```bash
pipenv shell
```

Para salir del entorno virtual, solo hay que colocar el siguiente comando:

```bash
exit
```

Para que visualizar todas las dependencias que tienes instaladas en el proyecto, ejecutar el siguiente comando:

```bash
pipenv graph
```

Si compartimos el proyecto con otras personas, para que ellos instalen todas las paqueterías del entorno virtual, estando dentro de la carpeta donde se encuentran los archivos `Pipfile` y `Pipfile.lock`, ejecutar el siguiente comando:

```bash
pipenv install
```

Si queremos que se instalen las versiones especificas de las librerías con las que trabaja el proyecto, para esto hay que ignorar el archivo `Pipfile` y ejecutar el archivo `Pipfile.lock`, para esto hay que ejecutar el siguiente comando:

```bash
pipenv install --ignore-pipfile
```

## Librerias

Para instala una librería, se tiene que ejecutar:

```bash
pip install nombre-librería
```

Para desinstalar una librería, se tiene que ejecutar:

```bash
pip uninstall nombre-libreria
```

Para enlistar librerías instaladas, se tiene que ejecutar

```bash
pip list
```

### Pandas

Librearía para trabajar con procesamiento de datos en diferentes formatos como son **Excel**, **CSV**, **SQL**, **JSON**, entre otros. Documentación [pandas](https://pypi.org/project/pandas/)

Instalación de libreíra:

```dash
pip install pandas
```

### Paquetes para publicar paquetes 

Instalar las siguientes librerías de forma global para crear paqueterias y subirlas a `Pypi`. Documentación [Pypi](https://pypi.org/)

Instalación de librería:

```bash
pip install setuptools wheel twine
```

### BAC0

Paquete para leer y escribir redes BACnet IP. Documentación [BAC0](https://pypi.org/project/BAC0/)

Instalación de librería:

```bash
pip install BAC0
```
