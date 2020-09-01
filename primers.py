print("Nombres primers fins a N")
n = int(input("Indica N --> "))

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

print(primers)
