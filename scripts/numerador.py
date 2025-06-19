"""
Formateador de líneas de turno de habla para las
transcripciones empleadas en la tesis.
"""


def numerador(archivo="all_.txt"):
    # Leer las líneas a las que se les agregará el formato numerado
    with open(archivo, "r", encoding="utf8") as entrada:
        lineas: list = entrada.readlines()
    # Crear un nuevo archivo con las líneas formateadas
    with open("enum_.txt", "w", encoding="utf8") as salida:
        for lin, linea in enumerate(lineas, start=1):
            num_format = f"{lin:03}"
            salida.write(f"{num_format} {linea}")
    print("Lineas enumeradas correctamente!")


if __name__ == "__main__":
    numerador()
