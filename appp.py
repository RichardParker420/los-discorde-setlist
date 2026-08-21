from flask import Flask, render_template_string

app = Flask(__name__)

# --- CONFIGURACIÓN DE LA BANDA ---
DATOS_BANDA = {
    "nombre": "LOS DISCORDE",
    "imagen_url": "https://via.placeholder.com/400x200", # SEPUEDE CAMBIAR PARA ACTUALIZAR
    "setlist": [
        {"titulo": "Con calma","letra":"Intro\n\nNo siempre, tenemos que huir\nSi lo intentamos\nSi no hay nada más, ¿Por qué seguir?...\n\nVerso\n\nDejamos de engañarnos\nNo está funcionando\nIntentando acercarnos\nSolo nos alejamos\nNos tenemos que soltar\nNos tenemos que soltar\n\nCoro\n\nNo siempre, tenemos que huir\nSi lo intentamos...\nSi no hay nada más, ¿Por qué seguir?\n\nPuente\n\nCon calma, con calmaaa\n Con calma, con calmaaa\n  Con calma, con calmaaa\n  Con calma, con calmaaa\n\nCoro Final\n\nNo siempre,tenemos que huir \nSi lo intentamos... \nSi no hay nada más, ¿Por qué seguir? \nX2  "},
        {"titulo": "Tiempo","letra":"Verso\n\nBuscó la manera de avanzar\nIntentando ya no tropezar\nEl tiempo es diferente\nY siento que me miente\nSiempre el cambio es frecuente, frecuentel\n\nCoro\n\nQué sería de mí\nQuesería de ti\n Casi nadie conoce el final\n\nVerso\n\nEl tiempo, no te va, esperar\nEncontremos el momento\nDe hablar\n\nCoro\n\nQué sería de mí\nQuesería de ti\n Casi nadie conoce el final\nQué sería de mí\nQuesería de ti\n Casi nadie conoce el final "},
        {"titulo": "Quedate","letra":"Verso\n\nNo puedo creer\nQue te tuve de frente y nunca noté\n Lo que me perdí\n Por serle fiel y nada que ver \n Me sigo sintiendo\n De la misma forma que te dije\n  ayer Lo sigo queriendo\n Como la primera vez \n\nCoro\n\nQuédate como la primera vez\n Quédate como la primera vez \n\nVERSO\n\n Dime si tu sientes lo mismo\n Siempre que salimos los domingos\n Porque mentirnos\n Caer siempre en lo mismo ooh.\n\nCORO\n\n Quédate como la primera vez\n Quédate como la primera vez \nQuédate como la primera vez\n Quédate como la primera vez .\n\n X2"},
        {"titulo": "Desaparecer","letra":"Verso\n\nTú me conoces bien\n Cuando no hay nadie lo sé \nY me dejas ver\n Como es que me ves \nComo es que me ves\n intentando\n No salirnos de este cuarto\nY dejando\n las siluetas en el carro\n\nPuente\n\n Ya no hay excusas\n Para vernos hoy \n\nCoro\n\nNo podemos\n Dejarlo en eso\n Seguirnos viendo\n ¿Por qué desaparecer?\n\nVerso\n\nMe sabes enloquecer\nCon tu aroma Chanel\nQuisiera una noche más\nCon tú piel, tú piel.\n\nCORO\n\nNo podemos dejarlo en eso\n Seguirnos viendo\n ¿Por qué desaparecer?\nNo podemos\ndejarlo solo en eso\n seguirnos viendo\n ¿Por qué desaparecer?"},
        {"titulo": "Estás con el","letra":"Verso\n\nEncontrarte\nSin saber de ti (de ti),\nQuise descifrarte\nEntenderte y amarte\nSé que el tiempo\nNo regresará (aah),\nQuise dejar\nDe extrañarte (de extrañarte) \n\nPuente\n\n¿Cómo saber Si al final\nNo estás con él?\nQuiero entender\nPor qué te hace sentir bien\n\nCoro\n\nsi... al final\nNo estás Con él\nAaaah aaaah\nPorque te hace sentir bien\n\nPuente\n\nComprender que\nNo todo está bien\nSabes que te quería\nPero al final\nTe vas con él\n\nCoro\n\n¿Cómo saber si al final \nNo estás con él?\nQuiero entender\nPor qué te hace sentir bien\n¿Cómo saber Si al final\nestás con él\nAaaah aaaah\nPorque te hace sentir bien?"},
        {"titulo": "Sera porque te quiero","letra":"Verso\n\nSerá porque te quiero\nPor eso sufro tanto\nMi corazón sangrando\nDe llorar y llorar\n\nCoro\n\nSi así quiso el destino\nQue tú ya no me quieras\nQue tú ya ni siquiera\nSientas algo por mi\n\nCoro\n\nTe quiero con locura\nY tú indiferente\nY tu corazón nada siente\nAl ver el mío sufrir\n\nPuente\n\nSerá porque te quiero\nHe querido olvidarte\nY al querer arrancarte\nTe quiero mucho más\n\nCoro\n\nSi así quiso el destino\nQue tú ya no me quieras\nQue tú ya ni siquiera\nSientas algo por mi\n\nCoro\n\nTe quiero con locura\nY tú indiferente\nY tu corazón nada siente\nAl ver el mío sufrir."},
        {"titulo": "Joya","letra":"Verso\n\nIntento no verlo\nY solo actuar\nSin importar\nYo decidí estar\nCon lo que quedo atrás\n\nPuente\n\nDejemos los fantasmas\nLos intentos del momento\nY empezar a ver de nuevo\nLo que no siento\n\nCoro\n\n¿Qué sientes cuando no me ves?\nConmigo no mientes tan bien\nTodo es distinto y no lo sé, no lo sé\n\nVerso\n\nDejemos los años atrás \nQue ya no es así\nMe he dejado de mentir\n\nCoro\n\n¿Qué sientes cuando no me ves?\nconmigo no mientes tan bien\nTodo es distinto y no lo sé, no lo sé\n¿Qué sientes cuando no me ves?\nConmigo no mientes tan bien\nTodo es distinto y no lo sé, no lo sé."},
        {"titulo": "Si nos tenemos","letra":"Verso\nLa ciudad nos quedó algo lejos del hogar\nNos dimos cuenta al mirar atrás\nEl día y la noche por igual\nPoder escapar de ese lugar\nQue nos dejó usar la soledad\nPara cambiar lo que está mal\nY nunca volver\n\nCoro\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\n\nVerso\n\nCorriendo libre te veo pasar\nEn un planeta para habitar\nPero contigo quizás mañana\n\nCoro\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\n\nPuente\nSi nos tenemos al final (uh uh)\nSi nos movemos de lugar (uh uh)\nSi nos tenemos al final (uh uh)\nSi nos movemos de lugar (uh uh)\n\nCoro\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\nPoder imaginar lo que será\nSi nos movemos de luga\nY la necesidad de estar allá\nSi nos tenemos al final\nSi nos tenemos..."},
    ]
}

# DISEÑO DE LA INTERFAZ (HTML/CSS)
HTML_Toy = """
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
    return render_template_string(HTML_Toy, banda=DATOS_BANDA)

if __name__ == '__main__':
    app.run(debug=True)