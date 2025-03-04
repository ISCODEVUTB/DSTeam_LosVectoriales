import hashlib

USUARIOS_FILE = "usuarios.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    tipo = input("Ingrese el tipo de usuario (cliente, administrador, domiciliario): ").lower()

    if tipo not in ["cliente", "administrador", "domiciliario"]:
        print("Tipo de usuario no válido.")
        return
    
    if(tipo == "administrador"):
        codigo = int(input("Ingrese codigo de administrador: "))
        if(codigo not in cod_admin):
            print("Codigo no valido")
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
                print(f"Autenticación exitosa. Tipo de usuario: {tipo}")
                return tipo
    print("Usuario o contraseña incorrectos.")
    return None

def menu():
    while True:
        print("\n1. Registrar usuario\n2. Iniciar sesión\n3. Salir")
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


cod_admin = [123,321,456,654]
menu()
