'''
Converte el texto de una trascripción correctamente
formateada a una estructura simple json donde la
key es el número de línea de la transcripción y el valor
una cadena de texto que contiene el habla, comentarios o
acciones que la persona en cuestión realizó.
Pueden encontrarse comentarios globales que no corresponden
a ningún participante de la sesión.
'''
import json
def txt_to_jason(archivo:str):
    with open(archivo,'r',encoding='utf8') as entrada:
        lineas : str = entrada.readlines()
    datos = {}
    for linea in lineas:
        num = linea[:3]
        texto = linea[4:].strip()
        datos[num] = texto
    with open('15-08-2024.json','w',encoding='utf8') as salida:
        json.dump(datos, salida, indent=2, ensure_ascii=False)
    print('Archivo json generado')
if __name__ == '__main__':
    txt_to_jason(r'/home/dante/DATA/Tesis/Transcripciones/15_08_2025/enum_15-08-2024.txt')