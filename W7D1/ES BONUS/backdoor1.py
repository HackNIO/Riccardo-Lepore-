import socket
host = '127.0.0.1' 
port = 33333 

# Creare un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
# Connessione al server
    s.connect((host, port))
    print(f"Connesso a {host} sulla porta {port}")

# Invia un messaggio al server
    message = "Ciao dal client Python!\n"
    s.sendall(message.encode())

# Riceve una risposta dal server
    data = s.recv(1024)
    print(f"Risposta dal server: {data.decode()}")

except Exception as e:
    print(f"Errore durante la connessione: {e}")
finally:
# Chiude il socket
    s.close()