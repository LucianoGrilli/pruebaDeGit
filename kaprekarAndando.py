"""
cantCasos= int(input("Ingrese la cantidad de casos a resolver: "))
lista =[]
for x in range(cantCasos):
	print("Ingrese el caso: ",x+1)
	numeroIngreso = int(input("Intruducir un numero que sea de 4 dígitos y que tenga al menos 2 digitos diferentes: "))
	numeroResta =0
	for i in range(10):
		numeroIngreso="{:04d}".format(numeroIngreso)
		numGrande = "".join(sorted(numeroIngreso,reverse=True))
		numChico = "".join(sorted(numeroIngreso))
		numeroIngreso = int(numGrande) - int(numChico)
		if numeroIngreso == numeroResta:
			break
		numeroResta=numeroIngreso

	print("")
	lista.append(i)

print("Las iteraciones de cada caso fueron las siguientes: ")
print(lista[:])

este de arriba no es
-----------------------------------------------------------------------------
el de abajo si va
"""

#este si va
cantCasos= int(input("Ingrese la cantidad de casos a resolver: "))
lista =[]
bandera = False
bandera2 = False

for x in range(cantCasos):
    print("Ingrese el caso: ",x+1)
    numeroIngreso = int(input("Intruducir un numero que sea de 4 dígitos y que tenga al menos 2 digitos diferentes: "))
    if numeroIngreso == 6174:
    	bandera =True
    if numeroIngreso == 1111 or numeroIngreso == 2222 or numeroIngreso == 3333 or numeroIngreso ==4444 or numeroIngreso ==5555 or numeroIngreso == 6666 or numeroIngreso ==7777 or numeroIngreso == 8888 or numeroIngreso ==9999 or numeroIngreso == 0000:
        bandera2 =True

    numeroResta =0
    for i in range(10):
        numeroIngreso="{:04d}".format(numeroIngreso)
        numGrande = "".join(sorted(numeroIngreso,reverse=True))
        numChico = "".join(sorted(numeroIngreso))

        numeroIngreso = int(numGrande) - int(numChico)


        if bandera2 == True:
           i=8
           bandera2=False
           break


        if bandera == True:
           i=0
           bandera =False
           break

        if numeroIngreso == numeroResta:

           break

        numeroResta=numeroIngreso

    print("")
    lista.append(i)

print("Las iteraciones de cada caso fueron las siguientes: ")
print(lista[:])


