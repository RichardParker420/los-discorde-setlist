import os
from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURACIÓN DE LA BANDA ---
DATOS_BANDA = {
    "nombre": "LOS DISCORDE",
    "imagen_url": "/static/foto.jpg",
    "setlist": [
        {"titulo": "Con calma",            "duracion": 210, "letra": "Intro\n\nNo siempre, tenemos que huir\nSi lo intentamos\nSi no hay nada más, ¿Por qué seguir?...\n\nVerso\n\nDejamos de engañarnos\nNo está funcionando\nIntentando acercarnos\nSolo nos alejamos\nNos tenemos que soltar\nNos tenemos que soltar\n\nCoro\n\nNo siempre, tenemos que huir\nSi lo intentamos...\nSi no hay nada más, ¿Por qué seguir?\n\nPuente\n\nCon calma, con calmaaa\nCon calma, con calmaaa\nCon calma, con calmaaa\nCon calma, con calmaaa\n\nCoro Final\n\nNo siempre, tenemos que huir\nSi lo intentamos...\nSi no hay nada más, ¿Por qué seguir?\nX2"},
        {"titulo": "Tiempo",               "duracion": 200, "letra": "Verso\n\nBuscó la manera de avanzar\nIntentando ya no tropezar\nEl tiempo es diferente\nY siento que me miente\nSiempre el cambio es frecuente, frecuente\n\nCoro\n\nQué sería de mí\nQué sería de ti\nCasi nadie conoce el final\n\nVerso\n\nEl tiempo, no te va, esperar\nEncontremos el momento\nDe hablar\n\nCoro\n\nQué sería de mí\nQué sería de ti\nCasi nadie conoce el final\nQué sería de mí\nQué sería de ti\nCasi nadie conoce el final"},
        {"titulo": "Quédate",              "duracion": 215, "letra": "Verso\n\nNo puedo creer\nQue te tuve de frente y nunca noté\nLo que me perdí\nPor serle fiel y nada que ver\nMe sigo sintiendo\nDe la misma forma que te dije ayer\nLo sigo queriendo\nComo la primera vez\n\nCoro\n\nQuédate como la primera vez\nQuédate como la primera vez\n\nVerso\n\nDime si tú sientes lo mismo\nSiempre que salimos los domingos\nPorque mentirnos\nCaer siempre en lo mismo ooh.\n\nCoro\n\nQuédate como la primera vez\nQuédate como la primera vez\nQuédate como la primera vez\nQuédate como la primera vez\n\nX2"},
        {"titulo": "Desaparecer",          "duracion": 205, "letra": "Verso\n\nTú me conoces bien\nCuando no hay nadie lo sé\nY me dejas ver\nComo es que me ves\nComo es que me ves\nIntentando\nNo salirnos de este cuarto\nY dejando\nLas siluetas en el carro\n\nPuente\n\nYa no hay excusas\nPara vernos hoy\n\nCoro\n\nNo podemos\nDejarlo en eso\nSeguirnos viendo\n¿Por qué desaparecer?\n\nVerso\n\nMe sabes enloquecer\nCon tu aroma Chanel\nQuisiera una noche más\nCon tu piel, tu piel.\n\nCoro\n\nNo podemos dejarlo en eso\nSeguirnos viendo\n¿Por qué desaparecer?\nNo podemos\nDejarlo solo en eso\nSeguirnos viendo\n¿Por qué desaparecer?"},
        {"titulo": "Estás con él",         "duracion": 220, "letra": "Verso\n\nEncontrarte\nSin saber de ti (de ti),\nQuise descifrarte\nEntenderte y amarte\nSé que el tiempo\nNo regresará (aah),\nQuise dejar\nDe extrañarte (de extrañarte)\n\nPuente\n\n¿Cómo saber si al final\nNo estás con él?\nQuiero entender\nPor qué te hace sentir bien\n\nCoro\n\nSi... al final\nNo estás con él\nAaaah aaaah\nPorque te hace sentir bien\n\nPuente\n\nComprender que\nNo todo está bien\nSabes que te quería\nPero al final\nTe vas con él\n\nCoro\n\n¿Cómo saber si al final\nNo estás con él?\nQuiero entender\nPor qué te hace sentir bien\n¿Cómo saber si al final\nEstás con él?\nAaaah aaaah\nPorque te hace sentir bien"},
        {"titulo": "Será porque te quiero","duracion": 225, "letra": "Verso\n\nSerá porque te quiero\nPor eso sufro tanto\nMi corazón sangrando\nDe llorar y llorar\n\nCoro\n\nSi así quiso el destino\nQue tú ya no me quieras\nQue tú ya ni siquiera\nSientas algo por mí\n\nCoro\n\nTe quiero con locura\nY tú indiferente\nY tu corazón nada siente\nAl ver el mío sufrir\n\nPuente\n\nSerá porque te quiero\nHe querido olvidarte\nY al querer arrancarte\nTe quiero mucho más\n\nCoro\n\nSi así quiso el destino\nQue tú ya no me quieras\nQue tú ya ni siquiera\nSientas algo por mí\n\nCoro\n\nTe quiero con locura\nY tú indiferente\nY tu corazón nada siente\nAl ver el mío sufrir."},
        {"titulo": "Joya",                 "duracion": 195, "letra": "Verso\n\nIntento no verlo\nY solo actuar\nSin importar\nYo decidí estar\nCon lo que quedo atrás\n\nPuente\n\nDejemos los fantasmas\nLos intentos del momento\nY empezar a ver de nuevo\nLo que no siento\n\nCoro\n\n¿Qué sientes cuando no me ves?\nConmigo no mientes tan bien\nTodo es distinto y no lo sé, no lo sé\n\nVerso\n\nDejemos los años atrás\nQue ya no es así\nMe he dejado de mentir\n\nCoro\n\n¿Qué sientes cuando no me ves?\nConmigo no mientes tan bien\nTodo es distinto y no lo sé, no lo sé\n¿Qué sientes cuando no me ves?\nConmigo no mientes tan bien\nTodo es distinto y no lo sé, no lo sé."},
        {"titulo": "Si nos tenemos",       "duracion": 230, "letra": "Verso\n\nLa ciudad nos quedó algo lejos del hogar\nNos dimos cuenta al mirar atrás\nEl día y la noche por igual\nPoder escapar de ese lugar\nQue nos dejó usar la soledad\nPara cambiar lo que está mal\nY nunca volver\n\nCoro\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\n\nVerso\n\nCorriendo libre te veo pasar\nEn un planeta para habitar\nPero contigo quizás mañana\n\nCoro\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\n\nPuente\n\nSi nos tenemos al final (uh uh)\nSi nos movemos de lugar (uh uh)\nSi nos tenemos al final (uh uh)\nSi nos movemos de lugar (uh uh)\n\nCoro\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\nPoder imaginar lo que será\nSi nos movemos de lugar\nY la necesidad de estar allá\nSi nos tenemos al final\nSi nos tenemos..."},
    ]
}


@app.route('/')
def home():
    return render_template('index.html', banda=DATOS_BANDA)


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
