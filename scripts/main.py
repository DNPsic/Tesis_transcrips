"""
Programa para ejecutar los scripts necesarios para
1. Juntar el texto de los archivos de las
transcripciones que se encuentren en x directorio.
2. Enumerar cada línea en el archvo generado.
"""

import append_txts
import numerador

if __name__ == "__main__":
    dir_input = input("Ruta del directorio: ")
    append_txts.combinar_archivos_txt(dir_input)
    numerador.numerador()
