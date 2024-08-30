 Image Scraping

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
  
