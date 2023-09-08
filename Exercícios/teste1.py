nome = input("Qual seu nome? ")
altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))

imc = peso/altura ** 2

print ("Qual seu nome? ",nome)
print ("Qual sua altura? ",altura)
print ("Qual seu peso em kg? ",peso)
print (f"Seu IMC é:{imc:.1f}")


