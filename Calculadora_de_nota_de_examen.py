def promedio(Controles):
    return sum(Controles)/len(Controles)

def calculadora(Controles,Segunda=False):
    """
    Calcula la nota necesaria en el examen para pasar los ramos
    """
    i=0
    if Segunda:
        NF=3.65
    else:
        NF=3.95
    
    n=len(Controles)
    if n == 0:
        raise ZeroDivisionError

    PC=n/(n+2)
    PE=1-PC
    while i<n:
        j=0
        if Controles[i]=="wf":
            Controles.pop(i)
            while j<len(Controles):
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
