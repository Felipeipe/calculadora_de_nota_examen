import Calculadora_de_nota_de_examen as calc

print("")
print("Bienvenido a la calculadora de notas \n")

print("Cuentame tus notas de los controles (para ver si salvas o no) \n")

i=1
Controles=[]
c=1
print("si tiraste workflow en algún control, debes escribir 'wf' en el control en donde lo tiraste \n")
while c!="basta":
    c=input("a ver tu nota del c" + str(i) + " (escribe 'basta' para continuar) "+"\n")
    Controles.append(c)
    i+=1

a=input("te quieres ir a segunda? (s/n)")

if a=="s":
    a=True
else:
    a=False

NE=calc.calculadora(Controles,a)

if a:
    print("necesitas un " + str(NE) + "para pasar al examen de segunda")

else:
    print("necesitas un " + str(NE) + " para pasar")

input("nos vemos! (presiona enter para cerrar)")

    
