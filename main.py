# main.py
from crypto_util import cargar_llave, cifrar_contraseña, descifrar_contraseña
from database import inicializar_db, agregar_contraseña, obtener_contraseñas, eliminar_contraseña

def main():
    inicializar_db()
    key = cargar_llave()  # Cargar la clave generada

    while True:
        print("Gestor de Contraseñas")
        print("1. Añadir nueva contraseña")
        print("2. Mostrar todas las contraseñas")
        print("3. Eliminar contraseña")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            servicio = input("Servicio: ")
            nombre_usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            contraseña_cifrada = cifrar_contraseña(contraseña, key)
            agregar_contraseña(servicio, nombre_usuario, contraseña_cifrada)
        elif opcion == '2':
            contraseñas = obtener_contraseñas()
            for id, servicio, nombre_usuario, contraseña_cifrada in contraseñas:
                contraseña = descifrar_contraseña(contraseña_cifrada, key)
                print(f"ID: {id}, Servicio: {servicio}, Nombre de Usuario: {nombre_usuario}, Contraseña: {contraseña}")
        elif opcion == '3':
            id = input("ID de la contraseña a eliminar: ")
            eliminar_contraseña(id)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
