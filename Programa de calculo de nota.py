import Calculadora_de_nota_de_examen as calc

print("")
print("Bienvenido a la calculadora de notas \n")

print("Cuentame tus notas de los controles (para ver si salvas o no) \n")

i=1
Controles=[]
c=1
while True:
    try:
        PC=float(input("cuanto porcentaje vale los controles que estás dando? \n"))/100
        break
    except ValueError:
        print("eso no es un número, ingresa uno correcto")

print("si tiraste workflow en algún control, debes escribir 'wf' en el control en donde lo tiraste \n")
while True:
    try:
        c=input(f"a ver tu nota del c{i} (escribe 'basta' para continuar) \n")
        if c=="basta":
            break
        n=float(c)
        Controles.append(c)
        i+=1
    except ValueError:
        if c=='wf':
            Controles.append(c)
            i+=1
        else:
            print("\nDebes escribir la nota con decimales y dichos decimales separados por puntos, como :'3.3'\nTambien debe ser un número")
    

a=input("te quieres ir a segunda? (s/n)")

if a=="s":
    a=True
else:
    a=False

NE=calc.calculadora(Controles,PC,a)

if a:
    print(f"necesitas un {NE} para pasar al examen de segunda")

else:
    print(f"necesitas un {NE} para pasar")

input("nos vemos! (presiona enter para cerrar)")

    
