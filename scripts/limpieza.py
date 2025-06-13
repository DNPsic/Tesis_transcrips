'''
Limpieza del texto de las transcripciones
'''
import re

def limpiador_texto(archivo:str):
    with open(archivo, 'r', encoding='utf8') as entrada:
        lineas:list = entrada.readlines()
    # identificar líneas de habla de AH
    habla_AH:list = [lin for lin in lineas if re.search(pattern= r"AH: ", string=lin)]
    # identificar patrones a eliminar
    patrones:list = [
        r"#.*", # comentarios
        r"\(.*\)", # paréntesis y contenido
        r"/\w+/", # palabras entre barras
        r"/\. |\ ./"
    ]
    habla_limpia:list = []
    for lin in habla_AH:
        for patron in patrones:
            lin = re.sub(pattern=patron,repl='',string=lin)
        habla_limpia.append(lin)
    #print(habla_limpia)
    with open('limpia.txt','w',encoding='utf8') as salida:
        salida.writelines(habla_limpia)
if __name__ == '__main__':
    limpiador_texto(r'/home/dante/DATA/Tesis/Transcripciones/15_08_2025/enum_15-08-2024.txt')