from source.users_packages import register_user, authenticate_user

def main():
    while True:
        print("\n--- Sistema de Gestión de Paquetes ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            register_user()
        elif opcion == "2":
            authenticate_user()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()