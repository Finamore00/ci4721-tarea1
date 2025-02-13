# CI4721 - Tarea 1: Parser de JSON

Parser de JSON usando la librería de parsec.py para Python.

## Cómo ejecutar

Dado que el proyecto hace uso de la librería externa `parsec`, se recomienda el uso de entornos virtuales de Python para evitar conflictos con los paquetes nativos del sistema. Para más información ver [aquí](https://docs.python.org/3/library/venv.html).

Instalar la dependencia mediante el comando 

```
pip install -r requirements
```

Tras adquirir los archivos necesarios el parser puede ejecutarse mediante 

```
python parser.py
```

El programa no toma entrada. En su lugar el JSON a parsear se encuentra en la variable `example` dentro del script. Si se desea probar con algún otro JSON distinto se requiere cambiar manualmente el valor de la variable `example`.
