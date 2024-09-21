def analizar_sintactico(tokens):
    estructuras = []
    
    for token in tokens:
        estructura = {
            'linea': token['linea'],
            'tipo_estructura': token['valor']
        }
        if token['tipo'] == 'Palabra reservada':
            estructura['estructura_correcta'] = 'X'
            estructura['estructura_incorrecta'] = ''
        else:
            estructura['estructura_correcta'] = ''
            estructura['estructura_incorrecta'] = 'X'
        
        estructuras.append(estructura)
    
    return estructuras
