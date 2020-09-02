import math

print("ax^2 + bx + c = 0")

try:
	a = float(input("Coeficient a: "))
	b = float(input("Coeficient b: "))
	c = float(input("Coeficient c: "))
except ValueError:
	print("Le entrades han de ser numèriques")
	

print("Equació segon grau tipus -> "+str(a)+"x²+"+str(b)+"x+"+str(c)+"=0")


if (a == 0):
	if (b != 0):
		x_1 = -c/b
		print("Una solució")
		print("x_1 --> ", x_1)
	else:
		if (c != 0):
			print("Sense solució c = 0")
		else:
			print("0 = 0")
else:
	dis = b*b - 4*a*c
	if (dis >= 0):
		x_1 = (-b + math.sqrt(dis)) / 2*a
		x_2 = (-b - math.sqrt(dis)) / 2*a
		print("Dues solucions")
		print("x_1 --> ", x_1)
		print("x_2 --> ", x_2)
		if (b == 0):
			print("Infinites solucions, es mostren dos")
	else:
		print("No hi ha solució en R, buscar en C")
