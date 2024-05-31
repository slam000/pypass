# crypto_util.py
from cryptography.fernet import Fernet

def cargar_llave():
    return open("llave.key", "rb").read()

def cifrar_contraseña(contraseña, key):
    fernet = Fernet(key)
    contraseña_cifrada = fernet.encrypt(contraseña.encode())
    return contraseña_cifrada

def descifrar_contraseña(contraseña_cifrada, key):
    fernet = Fernet(key)
    contraseña_descifrada = fernet.decrypt(contraseña_cifrada).decode()
    return contraseña_descifrada
