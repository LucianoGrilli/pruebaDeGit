cantCasos = input("Ingrese la cantidad de casos a probar: ")  #ingresa el resultado como una cadena
for x in range(int(cantCasos)):  #lo casteamos a entero en el bucle for
	
	print("Ingrese el numero: ",x+1)
    numeroIngreso = input("Intruducir un numero que sea de 4 dígitos y que tenga al menos 2 digitos diferentes: ")
    numero = int(numeroIngreso)
    numeroResta=0
    for i in range(10):
	    numeroIngreso= "{:04d}".format(numero)  #pasamos el numero entero a 4 digitos (por si el usuario ingresa 12, por ejemplo)
	    numGrande = "".join(sorted(numeroIngreso,reverse=True))  #aca ordena de mayor a menor los dígitos del numero ingresado
	    numChico = "".join(sorted(numeroIngreso))  #aca ordena de menor a mayor los dígitosdel numero igresado
	    numero = int(numGrande) - int(numChico) #restamos ambos numeros
	    if numero == numeroResta:
	       break                #si el numero ingresado es igual a 0, sale del bucle
	    numeroResta = numero   #de no ser así, asignamos a numeroResta el valor de numero asi sigue iterando
	
print("")
print("resultado: ", numero, "Cantidad de iteraciones: ",i)



