import hashlib
import openpyxl
import os
from menu_u import menu_customer, menu_administrator, menu_domiciliary
op_n = "Opcion invalida"
USERS_FILE = "users.txt"
cod_admin = [123, 321, 456, 654]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    user = input("Ingrese el nombre de usuario: ")
    pin = input("Ingrese la contraseña: ")
    type = input("Ingrese el tipo de usuario (cliente, administrador, domiciliario): ").lower()

    if type not in ["cliente", "administrador", "domiciliario"]:
        print("Tipo de usuario no válido.")
        return
    
    if type == "administrador":
        code = int(input("Ingrese código de administrador: "))
        if code not in cod_admin:
            print("Código de administrador incorrecto.")
            return

    with open(USERS_FILE, "a") as file:
        file.write(f"{user},{hash_password(pin)},{type}\n")
    print("Usuario registrado con éxito.")

def authenticate_user():
    user = input("Ingrese su nombre de usuario: ")
    pin = input("Ingrese su contraseña: ")

    with open(USERS_FILE, "r") as file:
        for line in file:
            user, pass_hash, type = line.strip().split(",")
            if user == user and pass_hash == hash_password(pin):
                print(f"Autenticación exitosa. Bienvenido, {user} ({type}).")
                if type == "cliente":
                    menu_customer(user)
                elif type == "administrador":
                    menu_administrator(user)
                elif type == "domiciliario":
                    menu_domiciliary(user)
                return  
    print("Usuario o contraseña incorrectos.")
    
def update_d(cls, user):
        if not os.path.exists(cls.FILE_PATH):
            print("No hay paquetes guardados.")
            return

        wb = openpyxl.load_workbook(cls.FILE_PATH)
        ws = wb.active

        packages_user = []
        
        for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            if row[0] == user: 
                packages_user.append((row_idx, row))

        if not packages_user:
            print("No tienes paquetes registrados.")
            return

        print("\nTus productos:")
        for idx, (row_idx, package) in enumerate(packages_user, start=1):
            print(f"{idx}. {package[1]} | Precio: {package[2]} | Peso: {package[3]} | Tipo: {package[4]}")

        try:
            pcambio = int(input("\nSeleccione el número del paquete que desea cambiar: ")) - 1
            if pcambio < 0 or pcambio >= len(packages_user):
                print("Selección inválida.")
                return
        except ValueError:
            print("Entrada inválida. Debe ser un número.")
            return

        row_idx, package = packages_user[pcambio]

        print("\nSeleccione el dato que desea cambiar:")
        print(f"1. Nombre ({package[1]})")
        print(f"2. Precio ({package[2]})")
        print(f"3. Peso ({package[3]})")
        print(f"4. Tipo ({package[4]})")
        print(f"5. Contenido ({package[5]})")
        print(f"6. Categoría ({package[6]})")
        print(f"7. Dimensiones ({package[7]})")

        try:
            cambio = int(input("\nDigite el número de la opción a cambiar: "))
            if cambio < 1 or cambio > 7:
                print(op_n)
                return
        except ValueError:
            print(op_n)
            return

        nuevo_valor = input("Ingrese el nuevo valor: ")

        ws.cell(row=row_idx, column=cambio + 1, value=nuevo_valor)

        wb.save(cls.FILE_PATH)
        wb.close()
        
        print("Cambio realizado con éxito.")