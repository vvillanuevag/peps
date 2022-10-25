import random

def aleatorio():
	valor = random.randint(1,100)
	return( valor)

def correcto(num_oculto,num_dicho):
	if (num_oculto==num_dicho):
		print("El numero es correcto")
		return(0)
	else:
		print("El numero no es correcto")
		return(1)

def mayor_o_menor(num_oculto,num_dicho):
	if (num_oculto>num_dicho):
		print("El numero es mayor")
	else:
		print("El numero es menor")


		