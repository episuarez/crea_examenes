class Respuesta:
    def __init__(self, respuesta, informacion, es_correcta, url_imagen=None):
        self.respuesta = respuesta;
        self.informacion = informacion;
        self.es_correcta = es_correcta;
        self.url_imagen = url_imagen;

    def __eq__(self, otro_objeto) -> bool:
        return self.respuesta == otro_objeto.respuesta;

    def __gr__(self, otro_objeto) -> bool:
        return self.respuesta > otro_objeto.respuesta;