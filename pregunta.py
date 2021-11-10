import random

from respuesta import Respuesta


class Pregunta:
    def __init__(self, titulo, pregunta, respuestas):
        self.titulo = titulo;
        self.pregunta = pregunta;

        self.respuestas = [];
        for indice, valor in enumerate(respuestas):
            if indice == 0:
                self.respuestas.append(Respuesta(valor, "", True));
            elif valor.count("#") == 2:
                self.respuestas.append(Respuesta(valor.split("#")[0], valor.split("#")[1], False, valor.split("#")[2]));
            else:
                self.respuestas.append(Respuesta(valor.split("#")[0], valor.split("#")[1], False));

        self.posicion_correcta = [indice for indice, respuesta in enumerate(self.respuestas) if respuesta.es_correcta][0];

    def __repr__(self):
        return f"{self.__dict__}";
