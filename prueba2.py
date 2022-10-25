import prueba

b=prueba.aleatorio()
a=int(input("Introduce el numero entre 1 y 100"))
while (prueba.correcto(b,a)!=0):
	prueba.mayor_o_menor(b,a)
	a=int(input("Introduce el numero entre 1 y 100"))


