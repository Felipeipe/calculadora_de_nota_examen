import Calculadora_de_nota_de_examen as calc

print("")
print("Bienvenido a la calculadora de notas \n")

print("Cuentame tus notas de los controles (para ver si salvas o no) \n")

i=1
Controles=[]
c=1
PC=float(input("cuanto porcentaje vale los controles que estás dando? \n"))/100
print("si tiraste workflow en algún control, debes escribir 'wf' en el control en donde lo tiraste \n")
while True:
    c=input("a ver tu nota del c" + str(i) + " (escribe 'basta' para continuar) "+"\n")
    if c=="basta":
        break
    Controles.append(c)
    i+=1

a=input("te quieres ir a segunda? (s/n)")

if a=="s":
    a=True
else:
    a=False

NE=calc.calculadora(Controles,PC,a)

if a:
    print("necesitas un " + str(NE) + "para pasar al examen de segunda")

else:
    print("necesitas un " + str(NE) + " para pasar")

input("nos vemos! (presiona enter para cerrar)")

    
