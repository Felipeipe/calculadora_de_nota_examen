def promedio(Controles:list[float])->float:
    """
    Calcula el promedio de una lista, la cual contiene objetos de tipo 'int' o 'float'
    """
    return sum(Controles)/len(Controles)

def calculadora(Controles:list,PC:float,Segunda:bool=False)->float:
    """
    Calcula la nota necesaria en el examen para pasar los ramos
    """
    i=0
    if Segunda:
        NF=3.65
    else:
        NF=3.95

    PE=1-PC

    n=len(Controles)

    for nota in Controles:
        j=0
        if nota=="wf":
            Controles.remove(nota)
            while j<n:
                Controles[j]=float(Controles[j])
                j+=1
            NE=(NF-(PC/n)*sum(Controles))*(n/(n*PE+PC))
            return NE
        else:
            Controles[i]=float(Controles[i])
        i+=1
    
    prom=promedio(Controles)
    NE=(NF-PC*prom)/PE
    return NE
