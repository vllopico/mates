import sys

print("Nombres primers fins a N")

try:
	n = int(input("Indica N --> "))
	if n <= 1:
		negatiu = ValueError
		raise negatiu
except ValueError:
	print("L'entrada ha de ser un nombre natural > 1")
	sys.exit(1)

num = 2
primers = []
while (num <= n):
	es_primer = True
	div = 2
	while (div <= num/2):
		if ( num % div == 0):
			es_primer = False
		div = div+1
	if (es_primer):
		primers.append(num)
	num=num+1

#Imprimir llista amb els N nombres primers
print(primers)
