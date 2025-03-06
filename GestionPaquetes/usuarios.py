import hashlib
from gestion_p import ExcelPaquetes
from gestion_e import hacer_pedido
import auth

USUARIOS_FILE = "usuarios.txt"

cod_admin = [123, 321, 456, 654]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    tipo = input("Ingrese el tipo de usuario (cliente, administrador, domiciliario): ").lower()

    if tipo not in ["cliente", "administrador", "domiciliario"]:
        print("Tipo de usuario no válido.")
        return
    
    if tipo == "administrador":
        codigo = int(input("Ingrese código de administrador: "))
        if codigo not in cod_admin:
            print("Código de administrador incorrecto.")
            return

    with open(USUARIOS_FILE, "a") as file:
        file.write(f"{usuario},{hash_password(contraseña)},{tipo}\n")
    print("Usuario registrado con éxito.")

def autenticar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    with open(USUARIOS_FILE, "r") as file:
        for line in file:
            user, pass_hash, tipo = line.strip().split(",")
            if user == usuario and pass_hash == hash_password(contraseña):
                print(f"Autenticación exitosa. Bienvenido, {usuario} ({tipo}).")
                auth.usuario = usuario  
                if tipo == "cliente":
                    menu_cliente(usuario)
                elif tipo == "administrador":
                    menu_administrador(usuario)
                elif tipo == "domiciliario":
                    menu_domiciliario(usuario)
                return  
    print("Usuario o contraseña incorrectos.")

def menu_cliente(usuario):
    while True:
        print(f"\nMenú Cliente ({usuario})")
        print("1. Tus productos")
        print("2. Hacer pedido")
        print("3. Ver estado de pedidos")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Mostrando productos...")
        elif opcion == "2":
            print("Realizando un pedido...")
            hacer_pedido(usuario)
        elif opcion == "3":
            print("Mostrando tus pedidos pendientes...")
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

def menu_administrador(usuario):
    while True:
        print(f"\nMenú Administrador ({usuario})")
        print("1. Agregar producto")
        print("2. Ver pedidos")
        print("3. Gestionar usuarios")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregando un nuevo producto...")
        elif opcion == "2":
            print("Listando pedidos...")
        elif opcion == "3":
            print("Gestionando usuarios...")
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

def menu_domiciliario(usuario):
    while True:
        print(f"\nMenú Domiciliario ({usuario})")
        print("1. Ver pedidos")
        print("2. Actualizar informacion de pedido")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Mostrando pedidos asignados...")
        elif opcion == "2":
            print("Pedido marcado como entregado.")
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

def menu():
    while True:
        print("\nMenú Principal")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            autenticar_usuario()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menu()
