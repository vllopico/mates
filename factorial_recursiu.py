import sys

#Funció recursiva per a calcular el factorial de n
def factorial(n):
	if (n == 0):
		return 1
	else:
		return n * factorial(n-1)

try:
	num = int(input("Indica el nombre sencer per a calcular el seu factorial: "))
	if (num < 0):
		negatiu = ValueError()
		raise negatiu
except ValueError:
	print("L'entrada ha de ser un nombre natural ( >= 0)")
	sys.exit(1)

print(f"{num}! = {factorial(num)}")
