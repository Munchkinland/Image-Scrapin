document.getElementById('scrape-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir el envío por defecto del formulario

    const formData = new FormData();
    const query = document.getElementById('query').value.trim();
    const fileInput = document.getElementById('file');
    const submitButton = document.querySelector('input[type="submit"]');
    const spinner = document.getElementById('spinner');
    const progressText = document.getElementById('progress-text');

    // Deshabilitar el botón de búsqueda
    submitButton.disabled = true;

    // Verificar si hay una consulta o archivo cargado
    if (fileInput.files.length > 0) {
        formData.append('file', fileInput.files[0]);
    }

    if (query) {
        formData.append('query', query);
    }

    if (!fileInput.files.length && !query) {
        alert('Por favor, introduce un término de búsqueda o sube un archivo.');
        // Habilitar el botón de búsqueda si no hay entrada
        submitButton.disabled = false;
        return;
    }

    // Mostrar el spinner y el texto de progreso
    spinner.style.display = 'block';
    progressText.textContent = 'Iniciando scraping...';

    fetch('/scrape', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Ocultar el spinner y restablecer el estado del botón
        spinner.style.display = 'none';
        progressText.textContent = 'Scraping completado.';
        submitButton.disabled = false;

        // Limpiar la galería antes de añadir nuevas imágenes
        document.getElementById('gallery').innerHTML = '';

        for (const [name, urls] of Object.entries(data)) {
            if (urls.length > 0) {
                const cardElement = document.createElement('div');
                cardElement.classList.add('image-card');
                
                const imgElement = document.createElement('img');
                imgElement.src = urls[0]; // Ajusta esto según cómo recibes la URL
                cardElement.appendChild(imgElement);
                cardElement.appendChild(document.createTextNode(name));
                
                document.getElementById('gallery').appendChild(cardElement);
            }
        }

        // Mostrar botón de descarga si es necesario
        document.getElementById('downloadSection').style.display = 'block';
    })
    .catch(error => {
        console.error('Error durante el scraping:', error);
        // Ocultar el spinner y mostrar mensaje de error
        spinner.style.display = 'none';
        progressText.textContent = 'Error en la conexión.';
        submitButton.disabled = false;
    });
});
