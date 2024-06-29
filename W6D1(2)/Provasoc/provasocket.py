import socket 

SRV_ADDR = "10.0.2.15"
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print ("Server avviato! Aspetto la connessione ...")
connection, address = s.accept()
print (" Client connesso con l'indirizzo : ", address)
while 1:
    data = connection.recv(1024)
    if not data:break
    #connection.sendall(b' -- Messaggio ricevuto --\n')
    print (data.decode('utf-8'))
connection.close()

