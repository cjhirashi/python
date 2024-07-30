# Proyectos con Python

## Entornos virtuales

Los entornos virtuales sirvern para mantener aislados un entorno de trabajo en cada proyecto, con la intención de mantener versiones especificas de las librerías instaladas, para que cuando se utilice este proyecto no entre en conflicto con otro proyecto que utilice otras versiones de las librerías instaladas

Primero hay que instalar la siguiente librería

```bash
pip install pipenv
```

Una vez que contamos con la librería anterior, para crear un nuevo entorno de trabajo, dentro de la carpeta del proyecto que vamos a trabajar, instalar la primer librería utilizada ahora intercambiadon el instalador de **Python** `pip` por `pipenv`

```bash
pipenv instal django
```

Para ver la ruta donde creo la carpeta del entorno virtual, ejecutar el siguiente comando:

```bash
pipenv --venv
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

### Pandas

Librearía para trabajar con procesamiento de datos en diferentes formatos como son **Excel**, **CSV**, **SQL**, **JSON**, entre otros

Instalación de libreíra:

```dash
pip install pandas
```
