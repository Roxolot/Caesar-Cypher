
def cifrar(mensaje, llave, ABECEDARIO):
	nuevo_mensaje = ''
	letra = ''
	for i in mensaje:
		if i in ABECEDARIO:
			letra = ABECEDARIO.find(i)
			
			if letra + llave >= len(ABECEDARIO):
				nuevo_mensaje = nuevo_mensaje + ABECEDARIO[letra+llave - len(ABECEDARIO)]
			else:
				nuevo_mensaje = nuevo_mensaje + ABECEDARIO[letra+llave]
		else:
			nuevo_mensaje = nuevo_mensaje + i
	return nuevo_mensaje

def descifrar(mensaje, llave, ABECEDARIO):
	nuevo_mensaje = ''
	letra = ''
	for i in mensaje:
		if i in ABECEDARIO:
			letra = ABECEDARIO.find(i)
			
			if letra - llave < 0:
				nuevo_mensaje = nuevo_mensaje + ABECEDARIO[letra - llave + len(ABECEDARIO)]
			else:
				nuevo_mensaje = nuevo_mensaje + ABECEDARIO[letra - llave]
		else:
			nuevo_mensaje = nuevo_mensaje + i
	return nuevo_mensaje

def menu():
	while(True):
		ABECEDARIO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
		opcion = input("que opcion quieres?\n1. cifrar\n2. descifrar\n3. decifrar con bruteforce\n4. salir\n")
		mensaje = ""
		llave = ""
		resultado = ''

		if opcion == "1":
			mensaje = input("cual es tu mensaje? ")
			llave = int(input("cual es tu llave? (numerico): "))
			resultado = cifrar(mensaje, llave, ABECEDARIO)
			print(resultado)

		if opcion == "2":
			mensaje = input("cual es tu mensaje? ")
			llave = int(input("cual es tu llave? (numerico): "))
			resultado = descifrar(mensaje, llave, ABECEDARIO)
			print(resultado)

		if opcion == "3":
			mensaje = input("cual es tu mensaje? ")
			for i in range(len(ABECEDARIO)):
				resultado = descifrar(mensaje, i, ABECEDARIO)
				print(f"llave: {i} = {resultado}")
		if opcion == "4":
			break
if __name__ == "__main__":
	menu()