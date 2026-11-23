def texto_valido(texto, tamanho):
    letras = 0
    for letra in texto:
        if letra == "'":
            return False
        if letra == "\\":
            return False
        if letra != " ":
            letras += 1
    if letras == 0:
        return False
    if len(texto) > tamanho:
        return False
    return True
