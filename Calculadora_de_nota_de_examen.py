def promedio(Controles):
    return sum(Controles)/len(Controles)

def calculadora(Controles,Segunda=False):
    """
    Calcula la nota necesaria en el examen para pasar los ramos
    """
    if Segunda:
        NF=3.65
    else:
        NF=3.95
    
    n=len(Controles)
    if n == 0:
        raise ZeroDivisionError

    PC=n/(n+2)
    PE=1-PC
    prom=promedio(Controles)
    NE=(NF-PC*prom)/PE
    return NE
