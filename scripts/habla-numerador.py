'''
Formateador de líneas de turno de habla para las
transcripciones empleadas en la tesis.
'''


def numerador_habla(archivo):
    # Leer las líneas a las que se les agregará el formato numerado
    with open(archivo, "r", encoding="utf8") as entrada:
        lineas: str = entrada.readlines()
    # Crear un nuevo archivo con las líneas formateadas
    with open("enum_15-08-2024.txt", "w", encoding="utf8") as salida:
        for lin, linea in enumerate(lineas, start=1):
            num_format = f"{lin:03}"
            salida.write(f"{num_format} {linea}")
    print("Lineas enumeradas correctamente!")


if __name__ == '__main__':
    numerador_habla(
        r"/home/dante/DATA/Tesis/Transcripciones/15_08_2025/all_15-08-2024.txt"
    )
