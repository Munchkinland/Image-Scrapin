import os
import io
import re
import zipfile
import sqlite3
import requests
import pandas as pd
from flask import Flask, request, jsonify, render_template, send_file
from bs4 import BeautifulSoup
from flask_cors import CORS

# Crear instancia de la aplicación Flask
app = Flask(__name__)
CORS(app)

# Conectar a la base de datos SQLite (se creará si no existe)
DB_NAME = 'images.db'

# Crear la base de datos y tabla si no existen
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS images')
    c.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            image_data BLOB
        )
    ''')
    conn.commit()
    conn.close()

# Llamada para inicializar la base de datos
init_db()

# Función para descargar la imagen
def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

# Función para buscar imágenes en Bing
def search_images(query, num_images=1):
    search_url = f"https://www.bing.com/images/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching search results for {query}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('a', {'class': 'iusc'})
    
    img_urls = []
    for img_tag in image_tags:
        m = re.search(r'"murl":"(http[^"]+)"', str(img_tag))
        if m:
            img_url = m.group(1)
            img_urls.append(img_url)
            if len(img_urls) >= num_images:
                break

    return img_urls

# Función para guardar la imagen en la base de datos
def save_image_to_db(name, image_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO images (name, image_data) VALUES (?, ?)', (name, image_data))
    conn.commit()
    conn.close()

# Ruta para manejar la búsqueda de imágenes
@app.route('/scrape', methods=['POST'])
def scrape():
    query = request.form.get('query')
    file = request.files.get('file')
    result = {}

    if file:
        # Cargar todas las hojas del archivo Excel
        xls = pd.ExcelFile(file)
        sheet_names = xls.sheet_names
        for sheet_name in sheet_names:
            df = pd.read_excel(file, sheet_name=sheet_name)
            for index, row in df.iterrows():
                name = row.get('name')
                if not name:
                    continue
                print(f"Processing {name} from sheet {sheet_name}...")
                img_urls = search_images(name, num_images=1)
                if not img_urls:
                    img_urls = search_images(name + " wallpaper", num_images=1)
                if img_urls:
                    image_data = download_image(img_urls[0])
                    if image_data:
                        save_image_to_db(name, image_data)
                        result[name] = [img_urls[0]]
                else:
                    result[name] = []

    elif query:
        img_urls = search_images(query, num_images=1)
        if not img_urls:
            img_urls = search_images(query + " wallpaper", num_images=1)
        if img_urls:
            image_data = download_image(img_urls[0])
            if image_data:
                save_image_to_db(query, image_data)
                result[query] = [img_urls[0]]
        else:
            result[query] = []

    return jsonify(result)

# Ruta para descargar todas las imágenes como un archivo ZIP
@app.route('/download_images', methods=['GET'])
def download_images():
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name, image_data FROM images")
        images = cursor.fetchall()
        conn.close()

        for name, image_data in images:
            filename = f"{name}.jpg"
            zip_file.writestr(filename, image_data)

    zip_buffer.seek(0)
    return send_file(zip_buffer, as_attachment=True, download_name='images.zip', mimetype='application/zip')

# Ruta principal para renderizar la página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
