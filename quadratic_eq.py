
import math

print("ax^2 + bx + c = 0")
a = float(input("a coefficient: "))
b = float(input("b coefficient: "))
c = float(input("c coefficient: "))

print("Quadratic equation: "+str(a)+"x²+"+str(b)+"x+"+str(c)+"=0")


if (a == 0):
	if (b != 0):
		x_1 = -c/b
		print("One solution")
		print("x_1 --> ", x_1)
	else:
		if (c != 0):
			print("Without solution c = 0")
		else:
			print("0 = 0")
else:
	dis = b*b - 4*a*c
	if (dis >= 0):
		x_1 = (-b + math.sqrt(dis)) / 2*a
		x_2 = (-b - math.sqrt(dis)) / 2*a
		print("Two solutions")
		print("x_1 --> ", x_1)
		print("x_2 --> ", x_2)
		if (b == 0):
			print("Infinite solution, two possibles")
	else:
		print("There is no solution in R, search in C")
