from users_packages import update_d, authenticate_user, register_user
from management_e import place_order
from excel_creation import ExcelPackages
op_n = "opcion invalida"

def menu_customer(user):
    while True:
        print(f"\nMenú Cliente ({user})")
        print("1. Tus productos")
        print("2. Hacer pedido")
        print("3. Ver estado de pedidos")
        print("4. Editar productos")
        print("5. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Mostrando productos...")
        elif opcion == "2":
            print("Realizando un pedido...")
            place_order(user)
        elif opcion == "3":
            print("Mostrando tus pedidos pendientes...")
        elif opcion == "4" :
            update_d(ExcelPackages, user)  
        elif opcion == "5":
            print("Cerrando sesión...")
            break
        else:
            print(op_n)

def menu_administrator(user):
    while True:
        print(f"\nMenú Administrador ({user})")
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
            print(op_n)

def menu_domiciliary(user):
    while True:
        print(f"\nMenú Domiciliario ({user})")
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
            print(op_n)

def menu():
    while True:
        print("\nMenú Principal")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            register_user()
        elif opcion == "2":
            authenticate_user()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print(op_n)