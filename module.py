def factorielle(n):
	# Début fonction
	fact = 1
	for i in range(1,n+1):
		fact *=i 
	return fact
	# Fin fonction
# programme princîpal
m= int(input("Entrez un entier positif :"))
print("la factorielle de",m, "est",factorielle(m))