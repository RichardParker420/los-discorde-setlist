from flask import Flask, render_template_string

app = Flask(__name__)

# --- CONFIGURACIÓN DE TU BANDA ---
DATOS_BANDA = {
    "nombre": "TU BANDA AQUÍ",
    "imagen_url": "https://via.placeholder.com/400x200", # Puedes cambiar esto por un link real
    "setlist": [
        {"titulo": "Canción 1", "letra": "Letra de la primera canción...\nVerso 1\nCoro..."},
        {"titulo": "Canción 2", "letra": "Letra de la segunda canción...\nVerso 1\nCoro..."},
        {"titulo": "Canción 3", "letra": "Letra de la tercera canción...\nVerso 1\nCoro..."}
    ]
}

# --- DISEÑO DE LA INTERFAZ (HTML/CSS) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ banda.nombre }} - Setlist</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #121212; color: #ffffff; font-family: sans-serif; }
        .cancion-card { background-color: #1e1e1e; border-radius: 8px; margin-bottom: 1rem; }
        .letra { display: none; white-space: pre-line; color: #b3b3b3; padding: 1rem; border-top: 1px solid #333; }
    </style>
</head>
<body class="p-4">
    <header class="text-center py-6">
        <h1 class="text-3xl font-bold text-yellow-500">{{ banda.nombre }}</h1>
        <p class="text-gray-400">Escanea el QR y sigue la letra en vivo</p>
    </header>

    <main class="max-w-md mx-auto">
        {% for item in banda.setlist %}
        <div class="cancion-card">
            <button onclick="toggleLetra({{ loop.index }})" class="w-full text-left p-4 font-semibold text-lg flex justify-between items-center">
                {{ loop.index }}. {{ item.titulo }}
                <span id="icon-{{ loop.index }} text-yellow-500">+</span>
            </button>
            <div id="letra-{{ loop.index }}" class="letra">
                {{ item.letra }}
            </div>
        </div>
        {% endfor %}
    </main>

    <script>
        function toggleLetra(id) {
            const el = document.getElementById('letra-' + id);
            const icon = document.getElementById('icon-' + id);
            if (el.style.display === 'block') {
                el.style.display = 'none';
            } else {
                el.style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, banda=DATOS_BANDA)

if __name__ == '__main__':
    app.run(debug=True)