import re

RESERVED_KEYWORDS = ["for", "For"]

def analizar_lexico(codigo):
    tokens = []
    lines = codigo.split("\n")
    
    for linea_num, linea in enumerate(lines, start=1):
        words = linea.split()
        columna_num = 1
        
        for palabra in words:
            if palabra in RESERVED_KEYWORDS:
                tokens.append({
                    'tipo': 'Palabra reservada',
                    'valor': palabra,
                    'linea': linea_num,
                    'columna': columna_num
                })
            else:
                tokens.append({
                    'tipo': 'Identificador',
                    'valor': palabra,
                    'linea': linea_num,
                    'columna': columna_num
                })
            columna_num += len(palabra) + 1 
    
    return tokens
