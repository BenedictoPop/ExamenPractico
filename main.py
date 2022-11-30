print("************************\n******EXAMEN PRACTICO***\n************************")
print("************************")
print("")
nombre=str(input("Ingrese su nombre: "))
cantidad=int(input("Ingrese la cantidad de pantalones a llvar: "))

total = int(cantidad + 160.50)
cantidad=0
desc= 10

if cantidad <= 7:
    cant=int(total * desc)
    print("La cantidad del descuento es: ", cant)

elif cantidad <=10:
    canti=int(total * 0.25)
    print("La cantidad  del descuento  es de Q", canti)
else:
    print("El total será: ", total)
    print("No se descontará")