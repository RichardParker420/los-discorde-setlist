import os
from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURACIÓN DE LA BANDA ---
DATOS_BANDA = {
    "nombre": "LOS DISCORDE",
    "imagen_url": "/static/foto.jpg",
    "setlist": [
        {"titulo": "Con calma",            "duracion": 240, "letra": "No siempre, tenemos que huir\nSi lo intentamos\nSi no hay nada más, ¿Por qué seguir?...\n\nDejamos de engañarnos\nNo está funcionando\nIntentando acercarnos\nSolo nos alejamos\nNos tenemos que soltar\nNos tenemos que soltar\n\nNo siempre, tenemos que huir\nSi lo intentamos...\nSi no hay nada más, ¿Por qué seguir?\n\nCon calma, con calmaaa\nCon calma, con calmaaa\nCon calma, con calmaaa\nCon calma, con calmaaa\n\nNo siempre, tenemos que huir\nSi lo intentamos...\nSi no hay nada más, ¿Por qué seguir?\nX2"},
        {"titulo": "Reflejo",              "duracion": 170, "letra": "Cada vez, que leo tu nombre\n Quiero ver, si aún, me conoces\nEs que no puedo cambiar te\n No puedo evitar te\n Casi parece, que Sales de mi.\n\nCuántas veces necesitas\nDecir adios mí\nA mi no me importa que\nSean las veces qué quieras.\n\nY no puedo controlarlo\nQue digan lo que quieran\nA mí no me sale ser\nCómo si no quisiera.\n\nCuántas veces necesitas\nDecir adios\nA mi no me importa que\nSean las veces qué quieras.\n\nCuántas veces necesitas\nDecir adios\nA mi no me importa que\nSean las veces qué quieras.\n"},
        {"titulo": "Quédate",              "duracion": 240, "letra": "No puedo creer\nQue te tuve de frente y nunca noté\nLo que me perdí\nPor serle fiel y nada que ver\nMe sigo sintiendo\nDe la misma forma que te dije ayer\nLo sigo queriendo\nComo la primera vez\n\nQuédate como la primera vez\nQuédate como la primera vez\n\nDime si tú sientes lo mismo\nSiempre que salimos los domingos\nPorque mentirnos\nCaer siempre en lo mismo ooh.\n\nQuédate como la primera vez\nQuédate como la primera vez\nQuédate como la primera vez\nQuédate como la primera vez\n\nX2"},
        {"titulo": "Tiempo",               "duracion": 180, "letra": "Buscó la manera de avanzar\nIntentando ya no tropezar\nEl tiempo es diferente\nY siento que me miente\nSiempre el cambio es frecuente\nfrecuente.\n\nQué sería de mí\nQué sería de ti\nCasi nadie conoce el final\n\nEl tiempo,no te va, esperar\nEncontremos el momento\nDe hablar \n\nQué sería de mí\nQué sería de ti\nCasi nadie conoce el final\nQué sería de mí\nQué sería de ti\nCasi nadie conoce el final."},
        {"titulo": "Si nos tenemos",       "duracion": 237, "letra": "La ciudad nos quedó algo lejos del hogar\nNos dimos cuenta al mirar atrás\nEl día y la noche por igual\nPoder escapar de ese lugar\nQue nos dejó usar la soledad\nPara cambiar lo que está mal\nY nunca volver\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\n\nCorriendo libre te veo pasar\nEn un planeta para habitar\nPero contigo quizás mañana\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\n\nSi nos tenemos al final (uh uh)\nSi nos movemos de lugar (uh uh)\nSi nos tenemos al final (uh uh)\nSi nos movemos de lugar (uh uh)\n\nPoder imaginar lo que será\nSi nos tenemos al final\nY la necesidad de estar allá\nSi nos movemos de lugar\nPoder imaginar lo que será\nSi nos movemos de lugar\nY la necesidad de estar allá\nSi nos tenemos al final\nSi nos tenemos..."},
        {"titulo": "El mar",               "duracion": 183, "letra": "Caminando sobre hielo \nVoy detenimiento me\nSin saber porque\nNo estás aquí\nNo me preguntes\nPor qué?\nNo me permito olvidarme\nooh oohh.\n\nSiempre has sido tu\nLo supe en el mar\nY cada minuto\nFue un huracán\nY termine a tus pies.\n\nSe me acabó la voz\nY me perdí en el tiempo\nFue difícil caminar\nEncontrar te en medio del mar\nY no sabes cómo me perdí\nSin ti.\n\nSiempre has sido tu\nLo supe en el mar\nY cada minuto\nFue un huracán\nY termine a tus pies.\n\nSiempre has sido tu\nLo supe en el mar\nAhhh ahhh."},
        {"titulo": "Si no quieres verme",  "duracion": 201, "letra": "Yo solo quiero que me digas\nOtro vez si tienes tiempo\nDe que puedas encontrar\nUna nueva forma de sentir\nQue lo nuestro, va teniendo\nUn lugar. \n\nYo solo quiero que\nNo me dejes ir lento\nQue pueda decir\nLo que sienta y.\n\nSi no quiere verme\nSabre que has decidido\nPor los dos\nNo quiero perder te\nPero al final fue lo\nQue sucedió\nSi no quieres verme\nSi no quieres verme\n\nYo solo quiero que me digas\nDe una vez si tienes tiempo\nY que puedas encontrar\nUna nueva forma de sentir\nQue lo nuestro\nVa teniendo un final.\n\nYo solo quiero que\nNo me dejes ir lento\nQue pueda decir\nLo que sienta y.\n\nSi no quiere verme\nSabre que has decidido\nPor los dos\nNo quiero perder te\nPero al final fue lo\nQue sucedió\nSi no quieres verme\nSi no quiere verme\n\nYo solo quiero que\nNo me dejes ir lento\nQue pueda decir\nLo que sienta \nYo solo quiero que\nNo me dejes ir lento\n\nSi no quiere verme\nSabre que has decidido\nPor los dos\nNo quiero perder te\nPero al final fue lo\nQue sucedió\nSi no quieres verme\nAceptaré sin más tu decisión\nSi no quiere verme\nSi no quiere verme."},
        {"titulo": "Desaparecer",          "duracion": 223, "letra": "Tú me conoces bien\nCuando no hay nadie, lo sé\nY me dejas ver, como es que me ves\nComo es que me ves\nIntentando, no salirnos de este cuarto\nY dejando, las siluetas en el carro\nYa no hay excusas para vernos hoy\n\nNo podemos dejarlo solo en eso\nSeguirnos viendo\n¿Por qué desaparecer?\n\nMe sabes enloquecer\nCon tu aroma Chanel\nQuisiera una noche más con tú piel, tú piel\n\nNo podemos dejarlo solo en eso\nSeguirnos viendo\n¿Por qué desaparecer?nNo podemos dejarlo solo en eso\nSeguirnos viendo\n¿Por qué desaparecer?"},
    ]
}


@app.route('/')
def home():
    return render_template('index.html', banda=DATOS_BANDA)


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
