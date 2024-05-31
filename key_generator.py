# key_generator.py
from cryptography.fernet import Fernet

def generar_llave():
    return Fernet.generate_key()

def guardar_llave(key):
    with open("llave.key", "wb") as key_file:
        key_file.write(key)

if __name__ == "__main__":
    key = generar_llave()
    guardar_llave(key)
    print("Clave generada y guardada exitosamente.")
