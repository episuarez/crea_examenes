from flask import Flask, render_template, request

from examen import Examen
from pregunta import Pregunta

app = Flask(__name__);

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/obtener_examen/<tipo>", methods=["POST"])
def obtener_examen(tipo):
    examen = Examen();

    try:
        for pregunta in request.json["datos"].split("\n\n"):
            datos = pregunta.split("\n");

            titulo = datos[0].split("#")[0];
            pregunta = datos[0].split("#")[1];
            respuestas = datos[1:];

            examen.preguntas.append(Pregunta(titulo, pregunta, respuestas));
    except:
        return "Error: Revise el formato del examen, hay algo erróneo.";

    if tipo == "texto":
        return examen.obtener_texto();
    elif tipo == "gift":
        return examen.obtener_gift();

    return {"status": 200, "resultado": "sdf"};

app.run(debug=True);
