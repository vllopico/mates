#Conèixer si un nombre sencer es perfecte 
#Un nombre sencer és perfecte si la suma dels seus divisors es el mateix nombre
num = int(input("Indica el nombre: "))

div = 1
suma = 0

while (div <= num/2):
	if ( num % div == 0):
		suma += div
	div += 1

if (num == suma):
	print(f'{num} és un nombre perfecte')
else:
	print(f'{num} no és un nombre perfecte')
	
