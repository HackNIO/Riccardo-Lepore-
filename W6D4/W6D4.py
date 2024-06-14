import math 

def perimetro_quadrato():
	lato= float(input("inserisci il valore del lato"))
	perimetro = 4* lato 
	return perimetro 
def circonferenza_cerchio():
	raggio =float(input("inserisci il valore del lato"))
	circonferenza = 2 * math.pi * raggio
	return  circonferenza
def perimetro_rettangolo(): 
	base = float(input("inserisci la base del rettangolo"))
	altezza = float (input("inserisci l'altezza del rettangolo"))
	perimetro = 2 * (base + altezza) 
	return perimetro 

def main ():
	print ("scegli la figura di cui vuoi calcolare il perimetro  ")
	print ("1-->Quadrato")
	print ("2-->Cerchio")
	print ("3-->Rettangolo")

scelta = input("scegli la figura :\n1:Quadrato\n2:Cerchio\n3:Rettangolo ")

if scelta == "1" :
	perimetro=perimetro_quadrato()
	print ("il perimetro del quadrato è:",perimetro)
elif scelta== "2":
	circonferenza = circonferenza_cerchio()
	print ("il perimetro del cerchio è:",circonferenza)
elif scelta =="3":
	perimetro = perimetro_rettangolo()
	print ("il perimetro del rettangolo è:",perimetro)
else :
	print ("scelta non valida")
if __name__ == "__main__":
	 main()
