import random
import string


class Examen:
    def __init__(self):
        self.preguntas = [];

    def obtener_texto(self):
        random.shuffle(self.preguntas);
        
        for pregunta in self.preguntas:
            random.shuffle(pregunta.respuestas);

        resultado = "";

        for indice, pregunta in enumerate(self.preguntas):
            resultado += f"{pregunta.titulo}\n";
            resultado += f"{indice + 1}. {pregunta.pregunta}\n";

            for indice_respuesta, respuesta in enumerate(pregunta.respuestas):
                resultado += f"{string.ascii_lowercase[indice_respuesta]}) {respuesta.respuesta}\n";
            resultado += "\n";

        resultado += "Respuestas:\n";
        for indice, pregunta in enumerate(self.preguntas):
            resultado += f"{indice + 1}) {pregunta.posicion_correcta}\n";

        return resultado;

    def obtener_gift(self):
        random.shuffle(self.preguntas);

        resultado = "";

        for indice, pregunta in enumerate(self.preguntas):
            resultado += f"// pregunta: {indice + 1} nombre: {pregunta.titulo}\n";

            resultado += f"::{pregunta.titulo}::{pregunta.pregunta} {{\n";
            resultado += f"={pregunta.respuestas[0].respuesta}\n";

            for respuesta in pregunta.respuestas[1:]:
                resultado += f"~{respuesta.respuesta}\n";
                resultado += f"#{respuesta.informacion}\n";

            resultado += "}\n";


        return resultado;
