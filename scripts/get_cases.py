"""
Programa para recuperar líneas específicas del corpus
insertando una lista de integers cuando se pida.
"""


def get_input() -> list:
    """Regresa una lista de números formateados."""
    user_in = input(
        "Introduce los números de línea a recuperar separados por espacio: "
    )
    # Para que el formato funcione debemos convertir a int
    inputs = [int(x) for x in user_in.split()]
    # Formatear números con la convención del corpus
    casos = list(map(lambda x: f"{x:03}", inputs))
    # print(casos)
    return casos


def get_lines(archivo: str, casos: list) -> list:
    """Genera un archivo nuevo seleccionando las líneas de texto indicadas."""
    with open(archivo, "r", encoding="utf8") as arch_in:
        lineas_archivo: list = arch_in.readlines()
    # Generamos una lista para los casos que coinciden
    casos_hallados = [
        linea for caso in casos for linea in lineas_archivo if caso in linea
    ]
    # print(casos_hallados)
    return casos_hallados


def add_labels(casos: list) -> list:
    etiquetado = [
        f"REF:{caso[:4].rstrip("\n")}\nCASO: {caso[8:].rstrip("\n")}\nPRODUCCIÓN: \nESP: \nALT: \nPR: \nTR: \nRT: \nESTR: \nGRAM: \nPS: \n\n"
        for caso in casos
    ]
    # print(etiquetado)
    return etiquetado


def make_file(casos: list):
    nombre = input("Nombre del archivo nuevo: ")
    with open(f"{nombre}.txt", "w", encoding="utf8") as salida:
        salida.writelines(casos)


if __name__ == "__main__":
    entrada = get_input()
    casos = get_lines(
        "/home/dante/DATA/Tesis/Transcripciones/15_08_2024/OK_15-08-2024.txt", entrada
    )
    formateados = add_labels(casos)
    make_file(formateados)
