"""
Programa para preparar el texto de la transcripción
a un archivo .tex para posteriormente compilarlo
como pdf y agregarlo arl corpus.
"""

import os
import re


def txt_to_latex(salida="_2024.tex", archivo="enum_.txt"):
    """
    Función que permite convertir un archivo de texto .txt
    a un arvhio para LaTeX, escapando los símvolos especiales
    para que se pueda compilar el pdf.

    Args:
        salida (string): nombre del nuevo archivo.
        archivo (string): archivo o su directorio a convertir.

    """
    with open(archivo, "r", encoding="utf8") as entrada:
        lineas: list = entrada.readlines()
    lineas_modificadas: list = [
        f"\\section{{Sesión del de del 2024}}\n",
        "\\noindent\n",
        "Datos de la sesión:\n",
        "ID:\n",
        "Participantes:\n",
        "AH:\n",
        "D:\n",
        "DT:\n",
        "AC:\n",
        "\n",
        "\\noindent\n",
    ]
    lineas_modificadas.append("")
    for linea in lineas:
        linea = linea.rstrip("\n")  # Elimina el salto de línea existente
        linea = re.sub("_", "\\_", linea)  # Sustituye _ por \_
        linea = re.sub("#", "\\#", linea)  # Sustituye # por \#
        if not linea.endswith("\\"):  # Si no termina con \, añádelo
            linea += r"\\"
        lineas_modificadas.append(linea + "\n")  # Vuelve a agregar el salto de línea
    # print(lineas_modificadas)

    # Guardar el resultado en un archivo .tex
    try:
        with open(f"{salida}.tex", "w", encoding="utf-8") as arch_out:
            arch_out.writelines(lineas_modificadas)
        print(f"¡archivo '{salida}' generado con éxito!")
        print("ruta:", os.path.abspath(salida))
    except Exception as e:
        print(f"Error al guardar: {e}")


def main():
    txt_to_latex("archivolatex", "prueba1.txt")


if __name__ == "__main__":
    main()
