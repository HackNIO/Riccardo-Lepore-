import random
import string

def genera_password(tipo='semplice'):
    if tipo == 'semplice':
        # Genera una password semplice di 8 caratteri alfanumerici
        caratteri = string.ascii_letters + string.digits
        password = ''.join(random.choice(caratteri) for _ in range(8))
    elif tipo == 'complessa':
        # Genera una password complessa di 20 caratteri ASCII
        caratteri = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(caratteri) for _ in range(20))
    else:
        raise ValueError("Tipo di password non valido. Usa 'semplice' o 'complessa'.")
    
    return password

password_semplice = genera_password('semplice')
password_complessa = genera_password('complessa')

print("Password semplice:", password_semplice)
print("Password complessa:", password_complessa)