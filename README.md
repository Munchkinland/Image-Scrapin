 # Image Scraping

 ![web-scraping-introduction-1](https://github.com/user-attachments/assets/464cce46-9be1-4a01-bbde-9359742a07c8)

**Image Scraping** es una aplicación web que permite buscar y descargar imágenes de la web. Los usuarios pueden buscar imágenes basadas en consultas de texto o subir un archivo de Excel con nombres de imágenes para buscarlas automáticamente. Las imágenes descargadas se almacenan en una base de datos SQLite y se pueden descargar como un archivo ZIP.

## Funcionalidades

- **Búsqueda de Imágenes**: Permite buscar imágenes usando una consulta de texto.
- **Carga de Archivos**: Permite cargar un archivo de Excel con una lista de nombres para buscar imágenes asociadas.
- **Almacenamiento**: Las imágenes se almacenan en una base de datos SQLite.
- **Descarga en Lote**: Permite descargar todas las imágenes almacenadas en la base de datos como un archivo ZIP.

## Requisitos

- Python 3.x
- Flask
- Requests
- BeautifulSoup4
- pandas
- sqlite3
- Flask-CORS

## Instalación

1. **Clonar el Repositorio**

   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/Munchkinland/Image-Scraping.git

  Luego, navega al directorio del proyecto:

cd Image-Scraping

Instalar Dependencias

Se recomienda usar un entorno virtual. Si aún no tienes virtualenv, instálalo:

pip install virtualenv

Crea y activa un entorno virtual:

- virtualenv venv
- source venv/bin/activate  # En Windows: venv\Scripts\activate
  
Instala las dependencias necesarias:

- pip install -r requirements.txt

Iniciar la Aplicación

Ejecuta el servidor Flask con:

- python app.py
  
La aplicación estará disponible en http://127.0.0.1:5000.

Interfaz Web

- Página Principal: Accede a http://127.0.0.1:5000 para utilizar la interfaz web de la aplicación.
- Formulario de Búsqueda: Introduce una consulta o sube un archivo de Excel para buscar imágenes.
- Descarga de Imágenes: Después de realizar búsquedas, puedes descargar todas las imágenes almacenadas como un archivo ZIP.
  
Estructura del Proyecto
- app.py: Archivo principal que ejecuta la aplicación Flask.
- images.db: Base de datos SQLite que almacena las imágenes.
- templates/index.html: Plantilla HTML para la interfaz web.
- static/styles.css: Hoja de estilos
- static/script.js: Archivo Java Script
- requirements.txt: Archivo de dependencias de Python.

Clona el repositorio para trabajar en él:

- git clone https://github.com/Munchkinland/Image-Scraping.git

Crear una Rama

- git checkout -b nombre-de-tu-rama

Realiza tus cambios y haz un commit:

- git add .
- git commit -m "Descripción de tus cambios"
  
Empujar Cambios y Crear un Pull Request

- git push origin nombre-de-tu-rama
- Luego, ve a GitHub y crea un pull request para que tus cambios sean revisados.

Licencia

- Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
