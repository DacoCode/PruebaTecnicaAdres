# Proyecto Django: Procesamiento de Facturas en PDF y validaciones de datos en foramto txt

## Descripción
Este proyecto en Django permite la carga, procesamiento y validación de archivos PDF de facturas en PDF. Extrae información clave como el CUFE, número de páginas y peso del archivo, almacenándolos en la base de datos SQLite del proyecto.
Tambien realiza validacion de datos en columnas donde debe de cumplir unos parametros para ser validos. 

## Funcionalidades
- **Carga de archivos PDF**
- **Extracción del CUFE** mediante expresión regular
- **Almacenamiento de datos en SQLite**
- **Visualización de facturas procesadas** en una vista de Django
- **Validacion de datos de formato txt** 

## Requisitos
Asegúrarse de tener instalado:
- Python 3.8+
- Django 4+
- PyMuPDF


## Configuración
1. Clona el repositorio:
   ```bash
   git clone (https://github.com/DacoCode/PruebaTecnicaAdres.git)
   ```

3. Ejecuta migraciones y levanta el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Uso

### Punto1
1. **Subir un archivo txt** desde la interfaz web.
2. El sistema cuando se le de click en subir archivo automaticamente señalara los campos erroneos o mencionará que no hay errores
   
### Punto2
1. **Subir un archivo PDF** desde la interfaz web.
2. **El sistema extraerá automáticamente** la información relevante.
3. **Consulta las facturas procesadas** en la vista de Django.

