
# AWSmaker

_Programa que permite gestionar y configurar distintos Servicios de AWS._

 
Ventana de login           |  Ventana de S3
:-------------------------:|:-------------------------:
![Login_Window](https://github.com/Alexvidalcor/AWSmaker/blob/master/input/AWSMaker_1.gif?raw=true)  |  ![S3_Window](https://github.com/Alexvidalcor/AWSmaker/blob/master/input/AWSMaker_2.png?raw=true)


## Comenzando 🚀

_Para SO basados en Debian y Fedora._

Ver **Despliegue** para conocer como desplegar el proyecto.

## Comenzando 🚀

Servicios          |  Estado
:-------------------------:|:-------------------------:
Gestión credenciales  |  OK
AWS S3  |  OK
AWS EC2  |  En desarrollo


### Pre-requisitos 📋

_Acceso a los recursos del repositorio:_

```
git clone https://github.com/Alexvidalcor/AWSmaker

cd AWSmaker/
```


### Instalación 🔧

_Pasos para instalación de entorno y ejecución de programa._

* Caso distribuciones basadas en Debian:

```
python3 EnvCreate.py
```

* Caso Fedora:
```
python EnvCreate.py
```

_Activar el entorno Python generado:_

```
source <NombreEntorno>/bin/activate
```
_Ejecución del programa._

* Caso distribuciones basadas en Debian:

```
python3 main.py
```

* Caso Fedora:

```
python main.py
```


## Despliegue 📦

**Deploy en local:**

Ejecutar el archivo "EnvCreate.py" para implementar un entorno virtual de Python con las dependencias necesarias (a través de "requirements.txt").

Para desactivar el entorno de Python generado:

```
deactivate
```

## Construido con 🛠️

* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK para Python.
* [PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/) - Python GUI For Humans.

## Licencia 📄

Este proyecto está bajo la Licencia (GNU GPL-V3) - mira el archivo [LICENSE.md](LICENSE.md) para detalles.


---
⌨️ con ❤️ por [Alexvidalcor](https://github.com/Alexvidalcor) 😊