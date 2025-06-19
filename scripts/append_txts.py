"""Programa para juntar en un solo archivo
el texto de diferentes archivos que se
encuentran dentro del mismo directorio"""

import os

# Datos a agregar al inicio de cada archivo nuevo
meta: str = """Sesión del 09 de agosto del 2014.
ID: AH-0908-2024.
Participantes:
AH: Mujer de 65 años, informante.
D: Daniela Salinas, entrevistadora. 
DT: Dante Nava, entrevistador.
AC: Hombre, hijo de AH.
"""


def combinar_archivos_txt(directorio, archivo_salida="all_.txt"):
    """
    Combina el contenido de todos los archivos .txt en un directorio,
    ordenados por su nombre numérico, en un único archivo de salida.

    Args:
        directorio (str): Ruta al directorio con los archivos .txt
        archivo_salida (str): Nombre del archivo de salida combinado
    """
    # Obtener lista de archivos .txt en el directorio
    archivos = [f for f in os.listdir(directorio) if f.endswith(".txt")]

    # Ordenar los archivos numéricamente (01.txt, 02.txt, etc.)
    archivos.sort()
    print(archivos)

    # Abrir archivo de salida en modo escritura
    with open(archivo_salida, "w", encoding="utf-8") as outfile:
        # Procesar cada archivo en orden
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio, archivo)
            try:
                # Leer el archivo y escribir su contenido en el archivo de salida
                with open(ruta_archivo, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    # Añadir un salto de línea entre archivos si no termina con uno
                    outfile.write("\n")
                print(f"Archivo {archivo} procesado correctamente.")
            except Exception as e:
                print(f"Error al procesar {archivo}: {str(e)}")

    print(f"\n¡Proceso completado! Archivo combinado creado: {archivo_salida}")


# Ejemplo de uso
if __name__ == "__main__":
    directorio_input = input("Ruta del directorio con archivos .txt: ")
    combinar_archivos_txt(directorio_input)
