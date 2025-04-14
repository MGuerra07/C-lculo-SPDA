def determinar_nivel_protecao(risco):
    """
    Determina o nível de proteção com base no risco calculado.
    Substitua os critérios com base nas normas aplicáveis.
    """
    if risco > 75:
        return "Nível I - Alta proteção necessária"
    elif risco > 50:
        return "Nível II - Proteção moderada necessária"
    elif risco > 25:
        return "Nível III - Proteção básica necessária"
    else:
        return "Nível IV - Proteção mínima necessária"
