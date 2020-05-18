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


